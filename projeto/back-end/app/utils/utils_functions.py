from app.model.models import Usuario, Produto

def get_user_dict(user: Usuario) -> dict:
    item = {}
    item["id"] = user.id
    item["email"] = user.email
    item["nome_de_usuario"] = user.nome_de_usuario
    item["nome_completo"] = user.nome_completo
    item["cpf"] = user.cpf
    item["created_at"] = user.created_at
    item["updated_at"] = user.updated_at if user.updated_at else "not updated yet"
    return item

def get_all_users_dict(users: list[Usuario]) -> list[dict]:
    users_dict = []
    for user in users:
        item = {}
        item["id"] = user.id
        item["email"] = user.email
        item["nome_de_usuario"] = user.nome_de_usuario
        item["nome_completo"] = user.nome_completo
        item["cpf"] = user.cpf
        item["created_at"] = user.created_at
        item["updated_at"] = user.updated_at if user.updated_at else "not updated yet"
        users_dict.append(item)
    return users_dict

def get_product_dict(produto: Produto) -> dict:
    item = {}
    item["id"] = produto.id
    item["nome"] = produto.nome
    item["preco"] = produto.preco
    item["restaurante_id"] = produto.restaurante_id
    item["descricao"] = None if not produto.descricao else produto.descricao
    item["created_at"] = produto.created_at
    item["updated_at"] = produto.updated_at if produto.updated_at else "not updated yet"
    return item

def get_list_product_dict(produtos: list[Produto]) -> list[dict]:
    produtos_list = []
    for produto in produtos:
        produtos_list.append(get_product_dict(produto))
    return produtos_list