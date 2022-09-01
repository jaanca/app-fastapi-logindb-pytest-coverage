from fastapi import APIRouter, Depends, status
from app.schemas.user import User,  ShowUser, UserUpdate
from app.db.conn_postgres import get_db
from sqlalchemy.orm import Session
from typing import List
from app.repository import user
from app.common.oauth import get_current_user

router = APIRouter(
    prefix='/user',
    tags={'Users'}
)

@router.get('/',response_model=List[ShowUser],status_code=status.HTTP_200_OK)
def obtener_usuarios(db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    usuarios = user.obtener_usuarios(db)
    return usuarios

@router.post('/',status_code=status.HTTP_201_CREATED)
def crear_usuario(usuario:User,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    user.crear_usuario(usuario,db)
    return {'respuesta':'Usuario creado satisfactoriamente'}

@router.post('/{user_id}',response_model=ShowUser,status_code=status.HTTP_200_OK)
def obtener_usuario(user_id:int,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    usuario = user.obtener_usuario(user_id,db)
    return usuario

@router.delete('/{user_id}',status_code=status.HTTP_200_OK)
def eliminar_usuario(user_id:int,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    user.eliminar_usuario(user_id,db)
    return {'respuesta':'Usuario eliminado correctamente'}
    
    
# @router.put('/{user_id}') # Modificar campos nombrados de forma estática
@router.patch('/{user_id}',status_code=status.HTTP_200_OK) # Modificar campos nombrados de forma dinámica
def actualizar_usuario(user_id:int,updateUser:UserUpdate,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    user.actualizar_user(user_id,updateUser,db)
    return {'respuesta':'Usuario actualizado correctamente'}
