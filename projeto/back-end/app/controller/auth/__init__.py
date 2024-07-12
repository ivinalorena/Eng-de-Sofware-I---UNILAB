import json
from datetime import timedelta
from http import HTTPStatus

from flasgger import swag_from
from flask import Blueprint, jsonify, request
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
)
from pydantic import ValidationError
from werkzeug.security import check_password_hash, generate_password_hash

from app.config import Config
from app.repositor.usuario import UsuarioRepositor
from app.schemas import LoginSchema, UsuarioSchema
from app.schemas import RefreshTokenSchema as RefreshTokenSchema
from app.utils.utils_functions import get_user_dict

auth = Blueprint("auth", __name__, url_prefix=f"{Config.API_BASE_PATH}/auth")

repossitor = UsuarioRepositor()


@auth.route("/signup", methods=["POST"])
@swag_from("../../docs/auth/signup.yaml")
def register():

    try:
        dados = UsuarioSchema.model_validate_json(request.data)
        user_exist = repossitor.select_by_email(email=dados.email)

        if user_exist:
            return jsonify({
                "Error": "User already exists"
            }), HTTPStatus.BAD_REQUEST

        senha_hash = generate_password_hash(dados.senha)
        repossitor.create(email=dados.email, senha=senha_hash, nome_de_usuario=dados.nome_de_usuario,
                        nome_completo=dados.nome_completo, cpf=dados.cpf
                        )

        usuario = repossitor.select_by_email(dados.email)

        return jsonify({"message": "User created", "user": get_user_dict(usuario)}), HTTPStatus.CREATED

    except ValidationError as ex:
        msg = json.loads(ex.json(include_input=False, include_url=False))
        return jsonify({"Error": f"{msg}"}), HTTPStatus.BAD_REQUEST


@auth.route("/signin", methods=["POST"])
@swag_from("../../docs/auth/login.yaml")
def signin():
    try:
        dados_login = LoginSchema.model_validate_json(request.data)

        exist_user = repossitor.select_by_email(dados_login.nome_de_usuario)

        if not exist_user:
            return jsonify({"Error": "Bad credentials entered"}), HTTPStatus.BAD_REQUEST

        if not check_password_hash(exist_user.senha, dados_login.senha):
            return jsonify({"Error": "email or password entered is not valid"}), HTTPStatus.BAD_REQUEST

        token = create_access_token(exist_user.nome_de_usuario, expires_delta=timedelta(minutes=60))
        refresh_token = create_refresh_token(exist_user.nome_de_usuario, expires_delta=False)

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
@swag_from("../../docs/auth/refresh_token.yaml")
def refresh():
    nome_de_usuario = get_jwt_identity()
    new_token = create_access_token(identity=nome_de_usuario)
    return jsonify({
        "new_token": new_token
    }), HTTPStatus.OK
