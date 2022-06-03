from datetime import datetime

import peewee

from utils.db import db


# modelo de peewee para la base de datos
class Tlibros(peewee.Model):
    titulo = peewee.CharField(unique=True, index=True)
    autor = peewee.CharField(unique=True, index=True)
    genero = peewee.CharField()
    isbn = peewee.CharField()
    portada = peewee.CharField()
    fechaPublicacion = peewee.DateTimeField(default=datetime.now)
    
    class Meta:
        database = db
        