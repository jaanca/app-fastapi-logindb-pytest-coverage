from sqlalchemy.orm import Session
from app.db import models
from fastapi import HTTPException,status
from app.common.hashing import HashCrypt

def crear_usuario(usuario,db:Session):
    '''Description
    :param models.User: user model to create
    :param Session: db session
    '''
    try:
        usuario=usuario.dict()
        nuevo_usuario=models.User(
            username=usuario["username"],
            password=HashCrypt.EncryptPassword(usuario["password"]),
            nombre=usuario["nombre"],
            apellido=usuario["apellido"],
            direccion=usuario["direccion"],
            telefono=usuario["telefono"],
            correo=usuario["correo"]
        )
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Error creando usuario: {}'.format(e)
        )


def obtener_usuario(user_id,db:Session):
    '''Description
    :param int: user id
    :param Session: db session
    '''
    usuario = db.query(models.User).filter(models.User.id==user_id).first()
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No existe el usuario con el id: {}'.format(user_id)
        )
    return usuario
    

def eliminar_usuario(user_id,db:Session):
    '''Description
    :param int: user id
    :param Session: db session
    '''
    usuario = db.query(models.User).filter(models.User.id==user_id)
    if not usuario.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No existe el usuario con el id: {}'.format(user_id)
        )
    usuario.delete(synchronize_session=False)
    db.commit()

def obtener_usuarios(db:Session):
    '''Description
    :param Session: db session
    :return models.User: Model user
    '''
    usuarios = db.query(models.User).all()
    return usuarios

def actualizar_user(user_id,updateUser,db:Session):
    '''Description
    :param int: user id
    :param UserUpdate: Scheme to user for modif
    :param Session: db session
    '''
    usuario = db.query(models.User).filter(models.User.id==user_id)
    if not usuario.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No existe el usuario con el id: {}'.format(user_id)
        )
    usuario.update(updateUser.dict(exclude_unset=True)) # exclude_unset = solo actualice los campos que llegan
    db.commit()
