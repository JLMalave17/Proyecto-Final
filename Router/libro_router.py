from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from fastapi import Query
from fastapi import Path
from typing import List, Optional
from Schema import libro_schema
from Service import libro_service
from Schema.usuario_schema import User
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
    summary="Creacion de un nuevo libro"
)

# funcion de el endpoint indicamos que es necesario recibir el modelo de en forma del cuerpo dela peticion
def create_user(book: libro_schema.LibroBase = Body(...)):
    # description del endpoint para la el swugguer
    """
    ### Agregar una nuevo libro

    ### Args
    La app podra recivir los siguientes pararametros en JSON
    - Titulo: Titulo del Libro
    - Genero:  Genero del libro(Accion,aventuras,..)
    - Autor: Nombre del autor
    - Portada: URL de una imagen
    - Fecha de publicacion:  fecha de publicacion del libro
    - ISBN: codigo de identificacion del libro


    ### Returns
    - Mensaje de libro añadido y datos del libro
    """
    return libro_service.create_book(book)






@router.get(
    "/{libro_id}",
    tags=["Libros"],
    status_code=status.HTTP_200_OK,
    response_model=libro_schema.Libro,
    dependencies=[Depends(get_db)]
)
def get_libros(
    libro_id: int = Path(
        ...,
        gt=0
    ),
    
):
    return libro_service.get_libros(libro_id)



@router.delete(
    "/{libro_id}",
    tags=["Libros"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_libro(
    libro_id: int = Path(
        ...,
        gt=0
    ),
    
):
    libro_service.delete_libro(libro_id)

    return {
        'msg': 'Borrado de forma correcta'
    }



