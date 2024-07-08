from flask import Flask 
from app.controller.auth import auth 
from app.config import Config

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY= Config.SECRET_KEY
        )
    else:
        app.config.from_mapping(test_config)
        
    
    app.register_blueprint(auth)
    
    return app