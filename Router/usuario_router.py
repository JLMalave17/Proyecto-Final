from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from fastapi.security import OAuth2PasswordRequestForm
from Schema import usuario_schema
from Service import usuario_service
from Service import login_service
from Schema.token_schema import Token
from utils.db import get_db

# definimos ruta de la api
router = APIRouter(prefix="/PROYECTO-FINAL")
# declaramos el tipo del endpont en este caso post metadatos para el swugguer
@router.post(
    "/user/",
    # agrupacion en la documentacion
    tags=["Usuarios"],
    # codigo de devolucion cuando se efectua corectamente
    status_code=status.HTTP_201_CREATED,
    # indicamos el modelo de respuesta
    response_model=usuario_schema.User,
    # indicamos la conexion con la base de datos
     dependencies=[Depends(get_db)],
    # informacion de lo que hace el endpont
    summary="Creacion de un nuevo Usuario"
)

# funcion de el endpoint indicamos que es necesario recibir el modelo de en forma del cuerpo dela peticion
def create_user(user: usuario_schema.UserRegister = Body(...)):
    # description del endpoint para la el swugguer
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



@router.post(
    "/login",
    tags=["Usuarios"],
    response_model=Token
)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    ## Login para token de acceso

    ### Args
   La aplicacion recibe :
    - username: Nombre de usuario y el email
    - password: la contraseña

    ### Returns
    - el token de acceso
    """
    access_token = login_service.generate_token(form_data.username, form_data.password)
    return Token(access_token=access_token, token_type="bearer")