from flasgger import Swagger, swag_from
from flask import Flask
from flask_jwt_extended import JWTManager

from app.config import Config
from app.controller.auth import auth
from app.controller.pedido import pedidos
from app.controller.produto import produto
from app.controller.restaurante import restaurante
from app.controller.usuario import usuario
from app.swagger import swagger_config, template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=Config.SECRET_KEY
        )
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(auth)
    app.register_blueprint(usuario)
    app.register_blueprint(produto)
    app.register_blueprint(restaurante)
    app.register_blueprint(pedidos)

    Swagger(app=app, config=swagger_config, template=template)

    JWTManager(app)

    return app
