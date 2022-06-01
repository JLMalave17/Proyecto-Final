        
import peewee

from utils.db import db
from .Usuarios import Tuser
from .Libros import Tlibros

class TlistaLibros(peewee.Model):
    estadoLibro = peewee.BooleanField(default=False)
    favorito = peewee.BooleanField(default=False)
    usuario_id = peewee.ForeignKeyField(Tuser)
    libro_id = peewee.ForeignKeyField(Tlibros)
    
    class Meta:
        database = db
        
        