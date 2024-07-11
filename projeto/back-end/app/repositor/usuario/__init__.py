from app.database.connection import DBConnectionHandler
from app.model.models import Usuario
from sqlalchemy.orm.exc import NoResultFound


class UsuarioRepositor:
    def create(self, email, senha, nome_de_usuario, nome_completo, cpf):
        with DBConnectionHandler() as db:
            try:
                usuario = Usuario(email=email, senha=senha, 
                            nome_de_usuario=nome_de_usuario, nome_completo=nome_completo, cpf=cpf)
                db.session.add(usuario)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def select(self):
        with DBConnectionHandler() as db:
            try:
                usuarios = db.session.query(Usuario).all()
                return usuarios
            except Exception as ex:
                db.session.rollback()
                raise ex

    def select_by_id(self, id:int):
        with DBConnectionHandler() as db:
            try:
                usuario = db.session.query(Usuario).filter(Usuario.id==id).first()
                return usuario
            except NoResultFound:
                return None
            except Exception as exception:
                raise exception
        
    def select_by_email(self, email):
        with DBConnectionHandler() as db:
            try:
                usuario = db.session.query(Usuario).filter(Usuario.email==email).first()
                return usuario
            except NoResultFound:
                return None
            except Exception as ex:
                db.session.rollback()
                raise ex
        
    def select_by_nome_de_usuario(self, nome_de_usuario):
        with DBConnectionHandler() as db:
            try:
                usuario = db.session.query(Usuario).filter(Usuario.username==nome_de_usuario).first()
                return usuario
            except NoResultFound:
                return None
            except Exception as ex:
                db.session.rollback()
                raise ex
                
    def update(self, id:int, dados:dict):
        with DBConnectionHandler() as db:
            try:
                is_user_updated =db.session.query(Usuario).filter(Usuario.id==id).update(dados)
                db.session.commit()
                return is_user_updated
            except Exception as ex:
                db.session.rollback()
                raise ex
            
    def delete(self, id:int):
        with DBConnectionHandler() as db:
            try:
                counts = db.session.query(Usuario).filter(Usuario.id==id).delete()
                db.session.commit()
                return counts
            except Exception as ex:
                db.session.rollback()
                raise ex