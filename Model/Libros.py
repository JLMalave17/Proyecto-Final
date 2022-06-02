from datetime import datetime

import peewee

from utils.db import db


# modelo de peewee para la base de datos
class Tlibros(peewee.Model):
    titulo = peewee.CharField(unique=True, index=True)
    autor = peewee.CharField(unique=True, index=True)
    genero = peewee.CharField()
    isbn = peewee.IntegerField()
    portada = peewee.CharField()
    fechaPublicacion = peewee.DateTimeField()
    
    class Meta:
        database = db
        