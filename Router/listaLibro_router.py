from fastapi import APIRouter, Depends, Body
from fastapi import status


from Schema import libro_schema
from Schema import listaLibro_schema
from Service import listaLibro_service
from utils.db import get_db
from Schema.usuario_schema import User
from Service.login_service import get_current_user


router = APIRouter(prefix="/PROYECTO-FINAL")

@router.post(
    "/",
    tags=["Lista"],
    status_code=status.HTTP_201_CREATED,
    response_model=listaLibro_schema.Lista,
    dependencies=[Depends(get_db)]
)
def create_list(libro: libro_schema.libroLista = Body(...), current_user: User = Depends(get_current_user)):
    return listaLibro_service.create_list(libro, current_user)