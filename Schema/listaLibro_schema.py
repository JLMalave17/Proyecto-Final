    # Python
from datetime import datetime

# Pydantic
from pydantic import BaseModel
from pydantic import Field


# class ListaCreate(BaseModel):
    
    


class Lista(BaseModel):
    id: int = Field(...)
    favorito: bool = Field(default=False)
    leido: bool = Field(default=False)
    