import json
from http import HTTPStatus

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from pydantic import ValidationError

from app.config import Config
from app.repositor.restaurante import RestauranteRepositor
from app.schemas import RestauranteSchema
from app.utils.utils_functions import (
    get_list_restaurantes_dict,
    get_restaurante_dict,
)

restaurante = Blueprint("restaurante", __name__, url_prefix=f"{Config.API_BASE_PATH}/restaurantes")

repositorio = RestauranteRepositor()


@restaurante.route("/", methods=["POST"])
def create_restaurante():

    try:
        dados = RestauranteSchema.model_validate_json(request.data)
        restaurante_exist = repositorio.select_by_name(nome=dados.nome)

        if restaurante_exist:
            return jsonify({
                "Error": "restaurant already exists"
            }), HTTPStatus.BAD_REQUEST

        repositorio.create(nome=dados.nome)

        restaurante_data = repositorio.select_by_name(dados.nome)

        return jsonify({
            "message": "product created",
            "restaurante": get_restaurante_dict(restaurante_data)
        }), HTTPStatus.CREATED
    except ValidationError as ex:
        msg = json.loads(ex.json(include_input=False, include_url=False))
        return jsonify({"Error": f"{msg}"}), HTTPStatus.BAD_REQUEST


@restaurante.route("/<id>", methods=["GET"])
@jwt_required()
def get_restaurante(id):
    dados_restaurante = repositorio.select_by_id(id)
    if not dados_restaurante:
        return jsonify({
            "Error": "restaurante not exists"
        }), HTTPStatus.BAD_REQUEST

    return jsonify({
        "message": "product data retrieved",
        "user": get_restaurante_dict(dados_restaurante)
    }), HTTPStatus.OK


@restaurante.route("/", methods=["GET"])
@jwt_required()
def get_all_restaurantes():
    restaurantes = repositorio.select()
    return jsonify({
        "message": "restaurantes data retrived",
        "restaurantes": get_list_restaurantes_dict(restaurantes)
    }), HTTPStatus.OK


@restaurante.route("/<id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    restaurante = repositorio.select_by_id(id)
    if not restaurante:
        return jsonify({
            "Error": "restaurante not exists"
        }), HTTPStatus.BAD_REQUEST

    dados = request.json
    restaurante_updated = repositorio.update(id, dados)
    return jsonify({
        "message": "restaurante updated",
        "restaurante": get_restaurante_dict(restaurante_updated)
    }), HTTPStatus.CREATED


@restaurante.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    restaurante = repositorio.select_by_id(id)
    if not restaurante:
        return jsonify({
            "Error": "restaurante not exists"
        }), HTTPStatus.BAD_REQUEST

    is_restaurante_deleted = repositorio.delete(id)
    if is_restaurante_deleted:
        return jsonify({
            "message": "restaurante deleted",
        }), HTTPStatus.OK
