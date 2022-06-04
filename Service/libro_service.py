from fastapi import HTTPException, status
# importamos los modelas de la base de datos
from Model.Libros import Tlibros as BookModel
# importamos modelo de ususarios para validar datos
from Schema import libro_schema
from Schema import usuario_schema




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








def get_libros(libro_id):

    libro = BookModel.filter(BookModel.id == libro_id).first()
    if not libro :
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Libro no encontrado en la BD"
            )

  

    return libro_schema.Libro(   
        id=libro_id,     
        titulo = libro.titulo,
        isbn = libro.isbn,
        portada = libro.portada,
        genero = libro.genero,
        autor = libro.autor,
        # FechaPublicacion = libro.FechaPublicacion
)

    

def delete_libro(libro_id: int):
    libro = BookModel.filter(BookModel.id == libro_id).first()
    if not libro :
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Libro no encontrado en la BD"
            )

    libro.delete_instance()
