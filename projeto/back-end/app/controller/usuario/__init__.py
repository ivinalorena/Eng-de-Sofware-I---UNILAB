from app.config import Config
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.repositor.usuario import UsuarioRepositor
from http import HTTPStatus
from app.utils.utils_functions import get_user_dict, get_all_users_dict

usuario = Blueprint("usuario", __name__, url_prefix=f"{Config.API_BASE_PATH}/usuarios")

repositorio = UsuarioRepositor()

@usuario.route("/<id>", methods=["GET"])
@jwt_required()
def get_user(id):
    dados_usuario = repositorio.select_by_id(id)
    if not dados_usuario:
        return jsonify({
            "Error": "user not exists"
        }), HTTPStatus.BAD_REQUEST
        
    return jsonify({
        "message": "user data retrieved",
        "user": get_user_dict(dados_usuario)
    }),HTTPStatus.OK
    
    
@usuario.route("/", methods=["GET"])
@jwt_required()
def get_all_users():
    usuarios = repositorio.select()
    return jsonify({
        "message": "users data retrived",
        "usuarios": get_all_users_dict(usuarios)
    }), HTTPStatus.OK
    
    
@usuario.route("/<id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    usuario = repositorio.select_by_id(id)
    if not usuario:
        return jsonify({
            "Error": "user not exists"
        }), HTTPStatus.BAD_REQUEST
        
    dados = request.json
    is_user_updated = repositorio.update(id, dados)
    if is_user_updated:
        user_updated = repositorio.select_by_id(id)
        return jsonify({
            "message": "user updated",
            "usuario": get_user_dict(user_updated)
        }), HTTPStatus.CREATED
    
@usuario.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    usuario = repositorio.select_by_id(id)
    if not usuario:
        return jsonify({
            "Error": "user not exists"
        }), HTTPStatus.BAD_REQUEST
        
    is_user_deleted = repositorio.delete(id)
    if is_user_deleted:
        return jsonify({
            "message": "user deleted",
        }), HTTPStatus.OK