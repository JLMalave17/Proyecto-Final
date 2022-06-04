from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from Schema import libro_schema
from Schema import listaLibro_schema
from Service import listaLibro_service
from utils.db import get_db
from Schema.usuario_schema import User
from Service.login_service import get_current_user


# definimos ruta de la api
router = APIRouter(prefix="/PROYECTO-FINAL")
# declaramos el tipo del endpont en este caso post metadatos para el swugguer
@router.post(
    "/lista",
     # agrupacion en la documentacion
    tags=["Lista"],
     # codigo de devolucion cuando se efectua corectamente
    status_code=status.HTTP_201_CREATED,
      # indicamos el modelo de respuesta
    response_model=listaLibro_schema.Lista,
      # indicamos la conexion con la base de datos
    dependencies=[Depends(get_db)],
       # informacion de lo que hace el endpont
    summary="Creacion de una relacion ususario libro"
)
def create_list(libro: libro_schema.libroLista = Body(...), current_user: User = Depends(get_current_user)):
    return listaLibro_service.create_list(libro, current_user)







@router.get(
    "/ListaUsuarios/{libro_id}",
    tags=["Lista"],
    status_code=status.HTTP_200_OK,
    response_model=List[listaLibro_schema.ListaUsario],
    dependencies=[Depends(get_db)],
        # informacion de lo que hace el endpont
    summary="Mostar los libros que tenga agregado el usuario a su lista de libros"
)
def get_libros(
    favorito: Optional[bool] = Query(None),
    leido: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return listaLibro_service.get_libros(current_user, favorito, leido)










@router.get(
    "/ListaLibros/{libro_id}",
    tags=["Lista"],
    status_code=status.HTTP_200_OK,
    response_model=List[listaLibro_schema.ListaLibros],
    dependencies=[Depends(get_db)],
         # informacion de lo que hace el endpont
    summary="Mostar los usuarios que tenga agregado el libro a su lista de libros"
)

def get_usuarios(
    libro_id: int = Path(
        ...,
        gt=0
    ),
    favorito: Optional[bool] = Query(None),
    leido: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
    
    
):
    return listaLibro_service.get_usuarios (libro_id ,current_user, favorito, leido)










@router.patch(
    "/Favorito/{libro_id}",
    tags=["Lista"],
    status_code=status.HTTP_200_OK,
    response_model=listaLibro_schema.ListaLibro_Usuario,
    dependencies=[Depends(get_db)],
         # informacion de lo que hace el endpont
    summary="Cambiar el atributo favorito a verdadero "
)

def favorito(
    libro_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return listaLibro_service.update_status_favorito(True, libro_id, current_user)











@router.patch(
    "/No_Favorito/{libro_id}",
    tags=["Lista"],
    status_code=status.HTTP_200_OK,
    response_model=listaLibro_schema.ListaLibro_Usuario,
    dependencies=[Depends(get_db)],
    summary="Cambiar el atributo favorito a falso "
)
def no_favorito(
    libro_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return listaLibro_service.update_status_favorito(False, libro_id, current_user)








@router.patch(
    "/Leido/{libro_id}",
    tags=["Lista"],
    status_code=status.HTTP_200_OK,
    response_model=listaLibro_schema.ListaLibro_Usuario,
    dependencies=[Depends(get_db)],
     summary="Cambiar el atributo leido a verdadero "
)
def favorito(
    libro_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return listaLibro_service.update_status_leido(True, libro_id, current_user)









@router.patch(
    "/No_leido/{libro_id}",
    tags=["Lista"],
    status_code=status.HTTP_200_OK,
    response_model=listaLibro_schema.ListaLibro_Usuario,
    dependencies=[Depends(get_db)],
    summary="Cambiar el atributo leido a falso "
)
def no_favorito(
    libro_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return listaLibro_service.update_status_leido(False, libro_id, current_user)












@router.delete(
    "/Borrar_lista/{libro_id}",
    tags=["Lista"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)],
    summary="Borrar libro de lisata de usuario por el id del libro "
)
def delete_lista(
    libro_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    listaLibro_service.delete_lista(libro_id, current_user)

    return {
        'msg': 'Borrado de forma correcta'
    }

