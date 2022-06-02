from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from Schema import libro_schema
from Service import libro_service

from utils.db import get_db

# definimos ruta de la api
router = APIRouter(prefix="/PROYECTO-FINAL")
# declaramos el tipo del endpont en este caso post metadatos para el swugguer
@router.post(
    "/libro/",
    # agrupacion en la documentacion
    tags=["Libros"],
    # codigo de devolucion cuando se efectua corectamente
    status_code=status.HTTP_201_CREATED,
    # indicamos el modelo de respuesta
    response_model=libro_schema.Libro,
    # indicamos la conexion con la base de datos
     dependencies=[Depends(get_db)],
    # informacion de lo que hace el endpont
    summary="Create a new user"
)

# funcion de el endpoint indicamos que es necesario recibir el modelo de en forma del cuerpo dela peticion
def create_user(book: libro_schema.LibroBase = Body(...)):
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
    return libro_service.create_book(book)