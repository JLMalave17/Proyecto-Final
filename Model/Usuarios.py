import peewee

from utils.db import db

# modelo de peewee para la base de datos
class Tuser(peewee.Model):
    email = peewee.CharField(unique=True, index=True)
    username = peewee.CharField(unique=True, index=True)
    password = peewee.CharField()

    class Meta:
        database = db
        

