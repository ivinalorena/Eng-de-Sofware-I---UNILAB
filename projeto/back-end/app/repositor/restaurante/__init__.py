from app.database.connection import DBConnectionHandler
from app.model.models import Restaurante
from sqlalchemy.exc import NoResultFound


class RestauranteRepositor:
    def create(self, nome):
        with DBConnectionHandler() as db:
            try:
                restaurante = Restaurante(nome=nome)
                db.session.add(restaurante)
                db.session.commit()
                return Restaurante
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def select(self):
        with DBConnectionHandler() as db:
            try:
                restaurantes = db.session.query(Restaurante).all()
                return restaurantes
            except Exception as ex:
                db.session.rollback()
                raise ex

    def select_by_id(self, id:int):
        with DBConnectionHandler() as db:
            try:
                restaurante = db.session.query(Restaurante).filter(Restaurante.id==id).first()
                return restaurante
            except NoResultFound:
                return None
            except Exception as ex:
                raise ex
                
    def update(self, id:int, dados:dict):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Restaurante).filter(Restaurante.id==id).update(dados)
                db.session.commit()
            except Exception as ex:
                db.session.rollback()
                raise ex
            
    def delete(self, id:int):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Restaurante).filter(Restaurante.id==id).delete()
                db.session.commit()
            except Exception as ex:
                db.session.rollback()
                raise ex