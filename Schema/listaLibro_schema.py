    # Python
from datetime import datetime

# Pydantic
from pydantic import BaseModel
from pydantic import Field


# class ListaCreate(BaseModel):

class ListaLibros(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="EjemploNombre"
    )

  
    favorito: bool = Field(default=False)
    leido: bool = Field(default=False)


class ListaLibro_Usuario(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="EjemploNombre"
    )
    titulo: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="Titulo de ejemplo"
    )
  
    favorito: bool = Field(default=False)
    leido: bool = Field(default=False)




class ListaUsario(BaseModel):
    titulo: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="Titulo de ejemplo"
    )
    id: int = Field(...)
    favorito: bool = Field(default=False)
    leido: bool = Field(default=False)
    isbn: str = Field(
        ..., 
        min_length=13,
        max_length=13,
        example="123456789222"
    
    
    )
    portada: str = Field(...)

    genero: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="Accion"
    )
    autor: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="Carlos Autor"
    )
  
    FechaPublicacion: datetime = Field(default=datetime.now())
    


class Lista(BaseModel):
    id: int = Field(...)
    favorito: bool = Field(default=False)
    leido: bool = Field(default=False)
    