from app.model.models import Usuario

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