from Model.Usuarios import Tuser
from Model.Libros import Tlibros
from Model.ListaLibros import TlistaLibros

from utils.db import db
# funcion para crear la base de datos con los tres modelos creados
def create_tables():
    with db:
        db.create_tables([Tuser, Tlibros, TlistaLibros])