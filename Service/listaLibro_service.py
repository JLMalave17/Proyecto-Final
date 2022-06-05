from fastapi import HTTPException, status


from Schema import listaLibro_schema
from Schema import libro_schema
from Schema import usuario_schema

from Model.ListaLibros import TlistaLibros as ListaModel
from Model.Libros import Tlibros as LibrosModel
from Model.Usuarios import Tuser as UsuarioModel


def create_list(book: libro_schema.libroLista, user: usuario_schema.User):
    lista = ListaModel.filter((ListaModel.libro_id == book.id) & (ListaModel.usuario_id == user.id)).first()

    if lista:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya esta agragado en la librera"
        )
 
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

    if((favorito is None) and (leido is None) ):
        Libreria_Usuario = ListaModel.filter(ListaModel.usuario_id == user.id)
        if not Libreria_Usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no tiene libros en la estanteria"
            )
    elif((favorito is not None) and (leido is None)):
        Libreria_Usuario = ListaModel.filter((ListaModel.usuario_id == user.id) & (ListaModel.favorito == favorito))
        if(favorito == False):
            if not Libreria_Usuario:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Usuario no tiene libros en la estanteria que no sean favoritos"
                )
        else:
            if not Libreria_Usuario:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Usuario no tiene libros en la estanteria que sean favoritos"
                )

    elif((favorito is None) and (leido is not None)):
        Libreria_Usuario = ListaModel.filter((ListaModel.usuario_id == user.id) & (ListaModel.estadoLibro == leido))
        if(leido == False):
            if not Libreria_Usuario:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Usuario no tiene libros en la estanteria que no esten leidos"
                )
        else:
            if not Libreria_Usuario:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Usuario no tiene libros en la estanteria que esten leidos"
                )

    elif((favorito is not None) and (leido is not None)):
        Libreria_Usuario = ListaModel.filter((ListaModel.usuario_id == user.id) & (ListaModel.favorito == favorito) & (ListaModel.estadoLibro == leido))
        if((favorito == False) and (leido == False)):
            if not Libreria_Usuario:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Usuario no tiene libros en la estanteria que no sean favoritos y no esten leidos"
                )
        elif((favorito == True) and (leido == False)):
            if not Libreria_Usuario:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                )
        elif((favorito == False) and (leido == True)):
            if not Libreria_Usuario:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Usuario no tiene libros en la estanteria que no sean favoritos y que esten leidos"
                )
        elif((favorito == True) and (leido == True)):
            if not Libreria_Usuario:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Usuario no tiene libros en la estanteria que sean favoritos y que esten leidos"
                )
        

    lista_libros = []
    for estanteria in Libreria_Usuario:
        libro = LibrosModel.filter(LibrosModel.id == estanteria.libro_id).first()
        lista_libros.append(
            listaLibro_schema.ListaUsario(
                
                titulo = libro.titulo,
                favorito = estanteria.favorito,
                leido = estanteria.estadoLibro,
                isbn = libro.isbn,
                portada = libro.portada,
                genero = libro.genero,
                autor = libro.autor,
                FechaPublicacion = libro.fechaPublicacion
            )
        )

    return lista_libros









def get_usuarios( libro , user: usuario_schema.User, favorito: bool = None, leido: bool = None):

    if((favorito is None) and (leido is None) ):
        Libreria_Usuario = ListaModel.filter(ListaModel.libro_id == libro)
        if not Libreria_Usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no tiene libros en la estanteria"
            )
    elif((favorito is not None) and (leido is None)):
        Libreria_Usuario = ListaModel.filter((ListaModel.libro_id == libro) & (ListaModel.favorito == favorito))
        if(favorito == False):
            if not Libreria_Usuario:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Usuario no tiene libros en la estanteria que no sean favoritos"
                )
        else:
            if not Libreria_Usuario:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Usuario no tiene libros en la estanteria que sean favoritos"
                )

    elif((favorito is None) and (leido is not None)):
        Libreria_Usuario = ListaModel.filter((ListaModel.libro_id == libro) & (ListaModel.estadoLibro == leido))
        if(leido == False):
            if not Libreria_Usuario:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Usuario no tiene libros en la estanteria que no esten leidos"
                )
        else:
            if not Libreria_Usuario:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Usuario no tiene libros en la estanteria que esten leidos"
                )

    elif((favorito is not None) and (leido is not None)):
        Libreria_Usuario = ListaModel.filter((ListaModel.libro_id == libro) & (ListaModel.favorito == favorito) & (ListaModel.estadoLibro == leido))
        if((favorito == False) and (leido == False)):
            if not Libreria_Usuario:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Usuario no tiene libros en la estanteria que no sean favoritos y no esten leidos"
                )
        elif((favorito == True) and (leido == False)):
            if not Libreria_Usuario:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Usuario no tiene libros en la estanteria que  sean favoritos y que esten leidos"
                )
        elif((favorito == False) and (leido == True)):
            if not Libreria_Usuario:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Usuario no tiene libros en la estanteria que no sean favoritos y que esten leidos"
                )
        elif((favorito == True) and (leido == True)):
            if not Libreria_Usuario:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Usuario no tiene libros en la estanteria que sean favoritos y que esten leidos"
                )
        


    
    lista_libros = []
    for estanteria in Libreria_Usuario:
        usuarioLista = UsuarioModel.filter(UsuarioModel.id == estanteria.usuario_id).first()
        lista_libros.append(
            listaLibro_schema.ListaLibros(
                username = usuarioLista.username,
                favorito = estanteria.favorito,
                leido =  estanteria.estadoLibro
            )
        )


    return lista_libros







def update_status_favorito(favorito: bool, libro_id: int, user: usuario_schema.User):
    lista = ListaModel.filter((ListaModel.libro_id == libro_id) & (ListaModel.usuario_id == user.id)).first()
    book = LibrosModel.filter((LibrosModel.id == libro_id)).first()
    if not lista:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Libro no encontrado en la estanteria"
        )

    lista.favorito = favorito
    lista.save()

    return listaLibro_schema.ListaLibro_Usuario(
    username = user.username,
    titulo = book.titulo,
    favorito = lista.favorito,
    leido = lista.estadoLibro

    )












def update_status_leido(leido: bool, libro_id: int, user: usuario_schema.User):
    lista = ListaModel.filter((ListaModel.libro_id == libro_id) & (ListaModel.usuario_id == user.id)).first()
    book = LibrosModel.filter((LibrosModel.id == libro_id)).first()
    if not lista:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Libro no encontrado en la estanteria"
        )

    lista.estadoLibro = leido
    lista.save()

    return listaLibro_schema.ListaLibro_Usuario(
    username = user.username,
    titulo = book.titulo,
    favorito = lista.favorito,
    leido = lista.estadoLibro



    )













def delete_lista(libro_id: int, user: usuario_schema.User):
    lista = ListaModel.filter((ListaModel.libro_id == libro_id) & (ListaModel.usuario_id == user.id)).first()
    if not lista:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="lista no encontrada"
        )

    lista.delete_instance()








        
    