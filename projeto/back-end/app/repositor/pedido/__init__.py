from app.database.connection import DBConnectionHandler
from app.model.models import Pedido
from sqlalchemy.exc import NoResultFound



class PedidoRepositor:
    def create(self, usuario_id, restaurante_id, produto_id):
        with DBConnectionHandler() as db:
            try:
                pedido = Pedido(usuario_id=usuario_id, restaurante_id=restaurante_id, produto_id=produto_id)
                db.session.add(pedido)
                db.session.commit()
                return pedido
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def select(self):
        with DBConnectionHandler() as db:
            try:
                pedidos = db.session.query(Pedido).all()
                return pedidos
            except Exception as ex:
                db.session.rollback()
                raise ex

    def select_by_id(self, id:int):
        with DBConnectionHandler() as db:
            try:
                peidido = db.session.query(Pedido).filter(Pedido.id==id).first()
                return peidido
            except NoResultFound:
                return None
            except Exception as ex:
                raise ex
                
    def update(self, id:int, dados:dict):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Pedido).filter(Pedido.id==id).update(dados)
                db.session.commit()
            except Exception as ex:
                db.session.rollback()
                raise ex
            
    def delete(self, id:int):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Pedido).filter(Pedido.id==id).delete()
                db.session.commit()
            except Exception as ex:
                db.session.rollback()
                raise ex