from fastapi import HTTPException, status
from passlib.context import CryptContext
# importamos los modelas de la base de datos
from Model.Libros import Tlibros as BookModel
# importamos modelo de ususarios para validar datos
from Schema import libro_schema




def create_book(book: libro_schema.LibroBase):
    # buscamos en la base de datos si existe un libro con el mismo isbm
    get_Libro = BookModel.filter((BookModel.isbn == book.isbn)).first()
    # si es igual saltara una execcion
    if get_Libro:
        msg = "el libro ya existe"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )
    # guardamos los datos enviados en una instancia de los modelos de la base de datos
    db_book = BookModel(
        titulo = book.titulo,
        isbn = book.isbn,
        portada = book.portada,
        genero = book.genero,
        autor = book.autor,
        FechaPublicacion = book.FechaPublicacion,
    )
    # guardamos los datos en la base de datos
    db_book.save()
    # devolvemos una instancia del modelo user como respuesta
    return libro_schema.Libro(
        id = db_book.id,
        titulo = db_book.titulo,
        isbn = db_book.isbn,
        portada = db_book.portada,
        genero = db_book.genero,
        autor = db_book.autor,
        FechaPublicacion = db_book.FechaPublicacion,
    )