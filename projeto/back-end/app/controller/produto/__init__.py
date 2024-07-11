from app.config import Config
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.repositor.produto import ProdutoRepositor
from app.repositor.restaurante import RestauranteRepositor
from http import HTTPStatus
from app.utils.utils_functions import get_product_dict, get_list_product_dict
from app.schemas import ProdutoSchema
from pydantic import ValidationError
import json

produto = Blueprint("produto", __name__, url_prefix=f"{Config.API_BASE_PATH}/produtos")

repositorio = ProdutoRepositor()


@produto.route("/", methods=["POST"])
def create_product():
    
    try:
        dados =  ProdutoSchema.model_validate_json(request.data)
        product_exist = repositorio.select_by_name(nome=dados.nome)

        if product_exist:
            return jsonify({
                "Error": "Product already exists"
            }), HTTPStatus.BAD_REQUEST
        restaurante_repo = RestauranteRepositor()
        is_restaurante_valid = restaurante_repo.select_by_id(dados.restaurante_id)
        if not is_restaurante_valid:
            return jsonify({
                "Error": "Enter a valid restaurant id"
            }), HTTPStatus.BAD_REQUEST
            
        repositorio.create(nome=dados.nome, descricao=dados.descricao, preco=dados.preco, restaurante_id=dados.restaurante_id)
        
        product_data = repositorio.select_by_name(dados.nome)
        
        return jsonify({
            "message": "product created",
            "product": get_product_dict(product_data)
        }), HTTPStatus.CREATED
    except ValidationError as ex:
        msg = json.loads(ex.json(include_input=False, include_url=False))
        return jsonify({"Error": f"{msg}"}), HTTPStatus.BAD_REQUEST

@produto.route("/<id>", methods=["GET"])
@jwt_required()
def get_product(id):
    dados_produto = repositorio.select_by_id(id)
    if not dados_produto:
        return jsonify({
            "Error": "produto not exists"
        }), HTTPStatus.BAD_REQUEST
        
    return jsonify({
        "message": "product data retrieved",
        "user": get_product_dict(dados_produto)
    }),HTTPStatus.OK
    
    
@produto.route("/", methods=["GET"])
@jwt_required()
def get_all_products():
    produtos = repositorio.select()
    return jsonify({
        "message": "users data retrived",
        "produtos": get_list_product_dict(produtos)
    }), HTTPStatus.OK
    
    
@produto.route("/<id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    produto = repositorio.select_by_id(id)
    if not produto:
        return jsonify({
            "Error": "product not exists"
        }), HTTPStatus.BAD_REQUEST
        
    dados = request.json
    produto_updated = repositorio.update(id, dados)
    return jsonify({
        "message": "product updated",
        "produto": get_product_dict(produto_updated)
    }), HTTPStatus.CREATED
    
@produto.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    produto = repositorio.select_by_id(id)
    if not produto:
        return jsonify({
            "Error": "product not exists"
        }), HTTPStatus.BAD_REQUEST
        
    is_product_deleted = repositorio.delete(id)
    if is_product_deleted:
        return jsonify({
            "message": "product deleted",
        }), HTTPStatus.OK