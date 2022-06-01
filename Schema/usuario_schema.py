
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr


class UserBase(BaseModel):
    email: EmailStr = Field(
        ...,
        example="Ejemplo@ejemplo.com"
    )
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="EjemploNombre"
    )


class User(UserBase):
    id: int = Field(
        ...,
        example="5"
    )


class UserRegister(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example="contraseña_Indesifrafle_Ejemplo"
    )
