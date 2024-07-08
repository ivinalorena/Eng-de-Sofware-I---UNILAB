from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os 
from app.config import Config


dialect = Config.DB_DIALECT
driver = Config.DB_DRIVER
username = Config.DB_USERNAME
password = Config.DB_PASSWORD
port = Config.DB_PORT
host = Config.DB_HOST
database = Config.DB_NAME

connection_string = f"{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}"

class DBConnectionHandler:
    
    def __init__(self) -> None:
        self.__conection_string = connection_string
        self.__engine = self.__create_engine()
        self.session = None
    
    def __create_engine(self):
        engine = create_engine(self.__conection_string, echo=False)
        return engine
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exp_val, exc_tb):
        self.session.close()