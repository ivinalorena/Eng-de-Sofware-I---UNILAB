from datetime import datetime

from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from app.database.base import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_completo = Column(String(250), nullable=False)
    nome_de_usuario = Column(String(20), nullable=False, unique=True)
    senha = Column(Text(), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    cpf = Column(BigInteger, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())
    pedidos = relationship("Pedido", backref="pedido.id", passive_deletes=True)

    def __repr__(self) -> str:
        return f"Usuario({self.id}, {self.nome}, {self.nome_de_usuario}, {self.senha}, {self.email},{self.cpf})"


class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    status = Column(String(20), nullable=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)
    produto_id = Column(Integer, ForeignKey("restaurantes.id"))
    restaurante_id = Column(Integer, ForeignKey("restaurantes.id"))
    desconto = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now(), nullable=True)


class Restaurante(Base):
    __tablename__ = "restaurantes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(35), nullable=False)
    classificacao = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())
    produtos = relationship("Produto", backref="produtos.id", passive_deletes=True)


class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30), unique=True)
    descricao = Column(Text, nullable=True)
    preco = Column(BigInteger, nullable=False, doc="valores expressos em centavos")
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())
    restaurante_id = Column(Integer, ForeignKey("restaurantes.id", ondelete="CASCADE"), nullable=False)
