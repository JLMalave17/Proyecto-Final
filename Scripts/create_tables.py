from Model.Usuarios import Tuser
from Model.Libros import Tlibros
from Model.ListaLibros import TlistaLibros

from utils.db import db

def create_tables():
    with db:
        db.create_tables([Tuser, Tlibros, TlistaLibros])