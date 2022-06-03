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


router = APIRouter(prefix="/PROYECTO-FINAL")

@router.post(
    "/lista",
    tags=["Lista"],
    status_code=status.HTTP_201_CREATED,
    response_model=listaLibro_schema.Lista,
    dependencies=[Depends(get_db)]
)
def create_list(libro: libro_schema.libroLista = Body(...), current_user: User = Depends(get_current_user)):
    return listaLibro_service.create_list(libro, current_user)

@router.get(
    "/ListaUsuarios",
    tags=["Lista"],
    status_code=status.HTTP_200_OK,
    response_model=List[listaLibro_schema.ListaUsario],
    dependencies=[Depends(get_db)]
)
def get_libros(
    favorito: Optional[bool] = Query(None),
    leido: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return listaLibro_service.get_libros(current_user, favorito, leido)

@router.get(
    "/ListaLibros",
    tags=["Lista"],
    status_code=status.HTTP_200_OK,
    response_model=List[listaLibro_schema.ListaLibros],
    dependencies=[Depends(get_db)]
)
def get_usuarios(
    favorito: Optional[bool] = Query(None),
    leido: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user),
    libro: libro_schema.libroLista = Body(...)
    
):
    return listaLibro_service.get_usuarios ( current_user, favorito, leido, libro )

