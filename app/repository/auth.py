from sqlalchemy.orm import Session
from app.db import models
from fastapi import HTTPException,status
from app.common.hashing import HashCrypt
from app.common.jwt import create_access_token

def auth_user(usuario,db:Session):
    user = db.query(models.User).filter(models.User.username==usuario.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No existe el usuario {}'.format(usuario.username)
        )
    if not HashCrypt.DecryptVerifyPassword(usuario.password,user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Contraseña incorrecta'
        )

    access_token = create_access_token(
        data={"sub": usuario.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}