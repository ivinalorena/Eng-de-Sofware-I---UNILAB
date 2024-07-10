from pydantic import BaseModel, model_validator
from typing_extensions import Self
from pydantic_core import PydanticCustomError


class UsuarioSchema(BaseModel):
    nome_completo: str
    nome_de_usuario: str
    email: str
    cpf: int
    senha: str
    
    @model_validator(mode="after")
    def is_atributs_numbers_qual_to_5(self) -> Self:
        n_elemnts = len(self.__dict__.keys())
        print(n_elemnts)
        if n_elemnts > 5:
            raise PydanticCustomError("There must be only 5 atributs")
        return self

class LoginSchema(BaseModel):
    nome_de_usuario: str
    senha:str
    
class RefreshTokenSchema(BaseModel):
    token: str