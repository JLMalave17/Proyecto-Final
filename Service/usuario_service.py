

from fastapi import HTTPException, status

from passlib.context import CryptContext
# importamos los modelas de la base de datos
from Model.Usuarios import Tuser as UserModel
# importamos modelo de ususarios para validar datos
from Schema import usuario_schema


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def create_user(user: usuario_schema.UserRegister):
    # buscamos en la base de datos si existe usuario con ese nombre o email
    get_user = UserModel.filter((UserModel.email == user.email) | (UserModel.username == user.username)).first()
    # si es igual saltyara una execcion
    if get_user:
        msg = "Email ya esta registrado"
        if get_user.username == user.username:
            msg = "El nombre de usuario ya esta registrado"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )
    # guardamos los datos enviados en una instancia de los modelos de la base de datos
    db_user = UserModel(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password)
    )
    # guardamos los datos en la base de datos
    db_user.save()
    # devolvemos una instancia del modelo user como respuesta
    return usuario_schema.User(
        id = db_user.id,
        username = db_user.username,
        email = db_user.email
    )