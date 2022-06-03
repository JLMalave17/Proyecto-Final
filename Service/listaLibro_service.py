from fastapi import HTTPException, status
from Model.Usuarios import Tuser

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
def get_libros(user: usuario_schema.User, favorito: bool = None, leido: bool = None):

    if(favorito is None):
        Libreria_Usuario = ListaModel.filter(ListaModel.user_id == user.id).order_by(ListaModel.created_at.desc())
    else:
        Libreria_Usuario = ListaModel.filter((ListaModel.user_id == user.id) & (ListaModel.favorito == favorito)).order_by(ListaModel.created_at.desc())

    lista_libros = []
    for estanteria in Libreria_Usuario:
        a = Tlibros.filter(Tlibros.id == estanteria.libro_id)
        lista_libros.append(
            listaLibro_schema.ListaUsario(
                titulo = a.titulo,
                favorito = estanteria.favorito,
                leido = estanteria.leido,
                isbn = a.isbn,
                portada = a.portada,
                genero = a.genero,
                autor = a.autor,
                FechaPublicacion = a.FechaPublicacion,

               
            )
        )

    return lista_libros

def get_usuarios( book: libro_schema.Libro, user: usuario_schema.User, favorito: bool = None, leido: bool = None):

    if(favorito is None):
        Libreria_Usuario = ListaModel.filter(ListaModel.libro_id == book.id).order_by(ListaModel.created_at.desc())
    else:
        Libreria_Usuario = ListaModel.filter((ListaModel.libro_id == book.id) & (ListaModel.favorito == favorito)).order_by(ListaModel.created_at.desc())

    lista_libros = []
    for estanteria in Libreria_Usuario:
        a = Tuser.filter(Tuser.id == estanteria.usuario_id)
        lista_libros.append(
            listaLibro_schema.ListaUsario(
                username = a.username,
                favorito = estanteria.favorito,
                leido =  estanteria.leido
            )
        )

    return lista_libros
# def get_libro(libro_id: int, user: usuario_schema.User):
#     libro = TodoModel.filter((TodoModel.id == libro_id) & (TodoModel.user_id == user.id)).first()

#     if not libro:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="libro not found"
#         )

#     return todo_schema.Todo(
#         id = libro.id,
#         title = libro.title,
#         is_done = libro.is_done,
#         created_at = libro.created_at
#     )
        
    