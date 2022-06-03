from fastapi import HTTPException, status

from Schema import listaLibro_schema
from Schema import libro_schema
from Schema import usuario_schema

from Model.ListaLibros import TlistaLibros as ListaModel
from Model.Libros import Tlibros

# def get(book: libro_schema.libroLista):

    
#     L = Tlibros.filter(Tlibros.isbn == book.isbn)
    
    
    
#     libro = libro_schema.Librolista2(
#                 id = L.id,
#                 isbn = L.isbn,  
#     )
        

#     return libro

def create_list(book: libro_schema.libroLista, user: usuario_schema.User):
    # b = get (book)

    db_list = ListaModel(      
        usuario_id = user.id,
        libro_id=book.id,
        estadoLibro = False,
        favorito = False
    )

    db_list.save()

    return listaLibro_schema.Lista(
        id = db_list.id,
        favorito = db_list.favorito,
        leido = db_list.estadoLibro
    )