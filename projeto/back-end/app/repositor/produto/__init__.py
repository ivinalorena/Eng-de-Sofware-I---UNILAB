from app.database.connection import DBConnectionHandler
from app.model.models import Produto
from sqlalchemy.exc import NoResultFound


class ProdutoRepositor:
    def create(self, nome, descricao, preco, restaurante_id):
        with DBConnectionHandler() as db:
            try:
                produto = Produto(nome=nome, descricao=descricao, preco=preco, restaurante_id=restaurante_id)
                db.session.add(produto)
                db.session.commit()
                return produto
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def select(self):
        with DBConnectionHandler() as db:
            try:
                produtos = db.session.query(Produto).all()
                return produtos
            except Exception as ex:
                db.session.rollback()
                raise ex

    def select_by_id(self, id:int):
        with DBConnectionHandler() as db:
            try:
                produto = db.session.query(Produto).filter(Produto.id==id).first()
                return produto
            except NoResultFound:
                return None
            except Exception as ex:
                raise ex
                
    def update(self, id:int, dados:dict):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Produto).filter(Produto.id==id).update(dados)
                db.session.commit()
            except Exception as ex:
                db.session.rollback()
                raise ex
            
    def delete(self, id:int):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Produto).filter(Produto.id==id).delete()
                db.session.commit()
            except Exception as ex:
                db.session.rollback()
                raise ex