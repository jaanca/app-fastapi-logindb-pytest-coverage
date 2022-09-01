from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# User Model
class User(BaseModel):
    username:str
    password:str
    nombre:str
    apellido:str
    direccion:Optional[str]
    telefono:str
    correo:str
    creacion:datetime=datetime.now()

class UserUpdate(BaseModel):
    username:str = None
    password:str = None
    nombre:str = None
    apellido:str = None
    direccion:str = None
    telefono:str = None
    correo:str = None
    creacion:datetime = None

# User Model for search ID
class UserId(BaseModel):
    id:int

# For response model
class ShowUser(BaseModel):
    id:int
    username:str
    nombre:str
    correo:str
    class Config():
        orm_mode=True

class Login(BaseModel):
    username:str
    password:str
