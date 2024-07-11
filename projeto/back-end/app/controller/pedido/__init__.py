from app.config import Config
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.repositor.pedido import PedidoRepositor
from http import HTTPStatus
from app.utils.utils_functions import get_pedidos_dict, get_list_pedidos_dict
from app.schemas import PedidosSchema
from pydantic import ValidationError
import json

pedidos = Blueprint("pedidos", __name__, url_prefix=f"{Config.API_BASE_PATH}/pedidos")

repositorio = PedidoRepositor()

@pedidos.route("/", methods=["POST"])
def create_pedidos():
    try:
        dados =  PedidosSchema.model_validate_json(request.data)
        repositorio.create(usuario_id=dados.usuario_id,produto_id=dados.produto_id, restaurante_id=dados.restaurante_id)
        return jsonify({
            "message": "pedido created"
        }), HTTPStatus.CREATED
    except ValidationError as ex:
        msg = json.loads(ex.json(include_input=False, include_url=False))
        return jsonify({"Error": f"{msg}"}), HTTPStatus.BAD_REQUEST

@pedidos.route("/<id>", methods=["GET"])
@jwt_required()
def get_pedidos(id):
    dados_pedidos = repositorio.select_by_id(id)
    if not dados_pedidos:
        return jsonify({
            "Error": "pedidos not exists"
        }), HTTPStatus.BAD_REQUEST
        
    return jsonify({
        "message": "product data retrieved",
        "user": get_pedidos_dict(dados_pedidos)
    }),HTTPStatus.OK
    
    
@pedidos.route("/", methods=["GET"])
@jwt_required()
def get_all_pedidoss():
    pedidos = repositorio.select()
    return jsonify({
        "message": "pedidoss data retrived",
        "pedidoss": get_list_pedidos_dict(pedidos)
    }), HTTPStatus.OK
    
    
@pedidos.route("/<id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    pedidos = repositorio.select_by_id(id)
    if not pedidos:
        return jsonify({
            "Error": "pedidos not exists"
        }), HTTPStatus.BAD_REQUEST
        
    dados = request.json
    pedidos_updated = repositorio.update(id, dados)
    return jsonify({
        "message": "pedidos updated",
        "pedidos": get_pedidos_dict(pedidos_updated)
    }), HTTPStatus.CREATED
    
@pedidos.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    pedidos = repositorio.select_by_id(id)
    if not pedidos:
        return jsonify({
            "Error": "pedidos not exists"
        }), HTTPStatus.BAD_REQUEST
        
    is_pedido_deleted = repositorio.delete(id)
    if is_pedido_deleted:
        return jsonify({
            "message": "pedidos deleted",
        }), HTTPStatus.OK