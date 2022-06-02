# Python
from datetime import datetime

# Pydantic
from pydantic import BaseModel
from pydantic import Field


class LibroBase(BaseModel):
    titulo: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="Titulo de ejemplo"
    )
    # isbn: int = Field(
    #     ..., 
    #     min_length=13,
    #     max_length=13,
    #     example="123456789222"
    
    
    # )
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

class Libro(BaseModel):
    id: int = Field(
        ...,
        example="5"
    )