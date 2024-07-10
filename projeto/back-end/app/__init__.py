from flask import Flask 
from app.controller.auth import auth 
from app.config import Config
from flask_jwt_extended import JWTManager
from flasgger import Swagger, swag_from
from app.swagger import template, swagger_config

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY= Config.SECRET_KEY
        )
    else:
        app.config.from_mapping(test_config)
        
    
    app.register_blueprint(auth)
    
    Swagger(app=app, config= swagger_config, template=template)
    
    JWTManager(app)
    
    return app