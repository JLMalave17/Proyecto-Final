from datetime import datetime

import peewee

from utils.db import db


# modelo de peewee para la base de datos
class Tlibros(peewee.Model):
    titulo = peewee.CharField()
    autor = peewee.CharField()
    genero = peewee.CharField()
    isbn = peewee.CharField(unique=True, index=True)
    portada = peewee.CharField()
    fechaPublicacion = peewee.DateTimeField(default=datetime.now)
    
    class Meta:
        database = db
        