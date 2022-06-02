
from pydantic import BaseModel
from pydantic import Field
# importamos emailstr para validar los emails no validos
from pydantic import EmailStr

# modelos para validar datos 


# modelo para usuario base
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

# modelo con id(ereda de userBase)
class User(UserBase):
    id: int = Field(
        ...,
        example="5"
    )

# modelo para el registro
class UserRegister(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example="contraseña_Indesifrafle_Ejemplo"
    )
