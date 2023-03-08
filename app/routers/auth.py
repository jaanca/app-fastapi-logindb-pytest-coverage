from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.conn_postgres import get_db
from fastapi.security import OAuth2PasswordRequestForm
from app.services import auth

router = APIRouter(
    prefix='/login',
    tags={'Login'}
)

@router.post('/',status_code=status.HTTP_200_OK)
def login(usuario:OAuth2PasswordRequestForm= Depends(),db:Session=Depends(get_db)):
    token = auth.auth_user(usuario,db)
    return token


