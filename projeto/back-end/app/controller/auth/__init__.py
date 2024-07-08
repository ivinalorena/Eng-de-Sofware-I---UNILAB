from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.repositor.usuario import UsuarioRepositor
from app.utils.utils_functions import get_user_dict

auth = Blueprint("auth", __name__, url_prefix="/auth")

repossitor = UsuarioRepositor()

@auth.route("/signup", methods=["POST"])
def register():
    dados = request.json
    user_exist = repossitor.select_by_email(email=dados["email"])

    if user_exist:
        return jsonify({
            "Error": "User already exists"
        }), 400
    
    senha_hash = generate_password_hash(dados["senha"])
    usuario = repossitor.create(email=dados["email"], senha=senha_hash, nome_de_usuario=dados["nome_de_usuario"],
                      nome_completo=dados["nome_completo"], cpf=dados["cpf"]
                      )
    
    return jsonify(
        {
            "message": "User created",
            "user": get_user_dict(usuario)
        }
    ), 201


@auth.route("/signin", methods=["POST"])
def signin():
    pass


@auth.route("/refresh", methods=["GET", "POST"])
def refresh():
    pass