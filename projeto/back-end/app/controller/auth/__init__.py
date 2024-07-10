from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.repositor.usuario import UsuarioRepositor
from app.utils.utils_functions import get_user_dict
from pydantic import ValidationError
from http import HTTPStatus
from app.schemas import UsuarioSchema, LoginSchema, RefreshTokenSchema
import json
from datetime import timedelta
from flask_jwt_extended import(
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    
)
from flasgger import swag_from


auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")

repossitor = UsuarioRepositor()

@swag_from("../../docs/auth/signup.yaml")
@auth.route("/signup", methods=["POST"])
def register():
    
    try:
        dados =  UsuarioSchema.model_validate_json(request.data)
        user_exist = repossitor.select_by_email(email=dados.email)

        if user_exist:
            return jsonify({
                "Error": "User already exists"
            }), HTTPStatus.BAD_REQUEST
        
        senha_hash = generate_password_hash(dados.senha)
        usuario = repossitor.create(email=dados.email, senha=senha_hash, nome_de_usuario=dados.nome_de_usuario,
                        nome_completo=dados.nome_completo, cpf=dados.cpf
                        )
        
        return jsonify({"message": "User created", "user": get_user_dict(usuario)} ), HTTPStatus.CREATED
    
    except ValidationError as ex:
        msg = json.loads(ex.json(include_input=False, include_url=False))
        return jsonify({"Error": f"{msg}"}), HTTPStatus.BAD_REQUEST

@swag_from("../../docs/auth/login.yaml")
@auth.route("/signin", methods=["POST"])
def signin():
    try:
        dados_login = LoginSchema.model_validate_json(request.data)
        
        exist_user = repossitor.select_by_email(dados_login.nome_de_usuario)
        
        if not exist_user:
            return jsonify({"Error": "Bad credentials entered"}), HTTPStatus.BAD_REQUEST
        
        if not check_password_hash(exist_user.senha, dados_login.senha):
            return jsonify({"Error": "email or password entered is not valid"}), HTTPStatus.BAD_REQUEST

        token = create_access_token(exist_user.nome_de_usuario, expires_delta=timedelta(minutes=5))
        refresh_token  = create_refresh_token(exist_user.nome_de_usuario, expires_delta=False)
        
        return jsonify({
            "message": "user is logged",
            "token": token,
            "refresh_token": refresh_token
        })
    except ValidationError as ex:
        msg = json.loads(ex.json(include_input=False, include_url=False))
        return jsonify({"Error": f"{msg}"}), HTTPStatus.BAD_REQUEST
    

@auth.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    nome_de_usuario = get_jwt_identity()
    new_token = create_access_token(identity=nome_de_usuario)
    return jsonify({
        "new_token": new_token
    }), HTTPStatus.OK