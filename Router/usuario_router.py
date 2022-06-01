from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from Schema import usuario_schema
from Service import usuario_service

from utils.db import get_db


router = APIRouter(prefix="/PROYECTO-FINAL")

@router.post(
    "/user/",
    tags=["users"],
    status_code=status.HTTP_201_CREATED,
    response_model=usuario_schema.User,
    dependencies=[Depends(get_db)],
    summary="Create a new user"
)
def create_user(user: usuario_schema.UserRegister = Body(...)):
    """
    ## Crear un nuevo usuario

    ### Args
    La app podra recivir los siguientes pararametros en JSON
    - email: Un email valido (la app lo comprobara)
    - username:  Un nombre de usuario
    - password: Una contraseña de autocomprobacion

    ### Returns
    - Los datos del usuario 
    """
    return usuario_service.create_user(user)