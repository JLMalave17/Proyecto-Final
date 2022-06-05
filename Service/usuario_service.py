
from fastapi import HTTPException, status

from passlib.context import CryptContext

from Model.Usuarios import Tuser as UserModel
from Schema import usuario_schema

# definimos variable para el hashe de contraseña
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# funcion de hash de contraseña
def get_password_hash(password):
    return pwd_context.hash(password)
# funcion para guardar usuario sen la bse de datoa recive com parametro userRegistre
def create_user(user: usuario_schema.UserRegister):
    # busqueda  en la base de datos si existe ya un usuario con esos datos
    get_user = UserModel.filter((UserModel.email == user.email) | (UserModel.username == user.username)).first()
    # si es asi mandamos un 400
    if get_user:
        msg = "Email ya esta registrado"
        if get_user.username == user.username:
            msg = "Usuario ya registrado"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )


# instancimos un modeo de peewee para la base de datos
    db_user = UserModel(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password)
    )
    # guardamos el usuario 
    db_user.save()
# devolvemos como respuesta que todo esta correcto bien un modelo pydantic
    return usuario_schema.User(
        id = db_user.id,
        username = db_user.username,
        email = db_user.email
    )

