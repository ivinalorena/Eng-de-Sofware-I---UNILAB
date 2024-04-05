import string
from typing import List
import services.database as db;
import models.cliente as Usuario;


def Incluir(usuario):
    count = db.cursor.execute("""
    INSERT INTO Usuarios (cliNome, cliIdade, cliSexo) 
    VALUES (?,?,?)""",
    usuario.nome, usuario.idade, usuario.sexo).rowcount
    db.cnxn.commit()
    
def SelecionarById(id):
    db.cursor.execute("SELECT * FROM Clientes WHERE ID = ?", id)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(Usuario.Usuario(row[0], row[1],row[2], row[3]))

    return costumerList[0]

def Alterar(usuario):
    print("alterando...")
    count = db.cursor.execute("""
    UPDATE Usuarios
    SET userNome = ?, userIdade = ?, userSexo = ?
    WHERE id = ?
    """,
    usuario.nome, usuario.idade, usuario.sexo, usuario.id).rowcount
    db.cnxn.commit()

def Excluir(id):
    count = db.cursor.execute("""
    DELETE FROM Usuarios WHERE id = ?""",
    id).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM Usuarios")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(Usuario.usuario(row[0], row[1],row[2], row[3]))
    return costumerList