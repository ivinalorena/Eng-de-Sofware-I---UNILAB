from app.model.models import Pedido, Produto, Restaurante, Usuario


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


def get_restaurante_dict(restaurante: Restaurante) -> dict:
    item = {}
    item["id"] = restaurante.id
    item["nome"] = restaurante.nome
    item["classificacao"] = None if not restaurante.classificacao else restaurante.classificacao
    item["created_at"] = restaurante.created_at
    item["updated_at"] = restaurante.updated_at if restaurante.updated_at else "not updated yet"
    # item["produtos"] = [] if not restaurante.produtos else restaurante.produtos
    return item


def get_list_restaurantes_dict(restaurantes: list[Restaurante]) -> list[dict]:
    restaurantes_list = []
    for restaurante in restaurantes:
        restaurantes_list.append(get_restaurante_dict(restaurante))
    return restaurantes_list


def get_pedidos_dict(peidio: Pedido) -> dict:
    item = {}
    item["id"] = peidio.id
    item["usuario_id"] = peidio.usuario_id
    item["restaurante_id"] = peidio.restaurante_id
    item["produto_id"] = peidio.produto_id
    item["created_at"] = peidio.created_at
    item["updated_at"] = peidio.updated_at if peidio.updated_at else "not updated yet"
    return item


def get_list_pedidos_dict(pedidos: list[Pedido]) -> list[dict]:
    pedidos_list = []
    for pedido in pedidos:
        pedidos_list.append(get_pedidos_dict(pedido))
    return pedidos_list
