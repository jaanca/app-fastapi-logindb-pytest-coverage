from fastapi.testclient import TestClient
import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

################################################
# TEST en SQLite para no impactar la base de datos de producción

################################################
# Importar los archivos del directorio principal
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

from main import app
from app.common.hashing import HashCrypt
from app.db.conn_postgres import get_db, Base

cliente = TestClient(app)

################################################
# Variables
usuario_app="andres"
usuario_clave="andres"
usuario_login = {
    "username":usuario_app,
    "password":usuario_clave
}

################################################
# Definir base de datos SQLite para las pruebas
db_path = os.path.join(os.path.dirname(__file__),'test.db')
db_uri = "sqlite:///{}".format(db_path)
SQLALCHEMY_DATABASE_URL = db_uri
engine_test = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False })
TestingSessionLocal = sessionmaker(bind=engine_test,autocommit=False,autoflush=False)
# Crear la base de datos desde cero
Base.metadata.create_all(bind=engine_test)

################################################
# Crear usuario inicial en la base de datos
def insertar_usuario_prueba():
    password_hash = HashCrypt.EncryptPassword(usuario_clave)
    engine_test.execute(
        f"""
        INSERT INTO usuario(username,password,nombre,apellido,direccion,telefono,correo)
        values
        ('{usuario_app}','{password_hash}','prueba_nombre','prueba_apellido','prueba_direccion',1212,'{usuario_app}@{usuario_app}')
        """
    )
insertar_usuario_prueba()

################################################
# Cambiar la configuración del API para conectarse a la base de datos nueva
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

################################################
# Casos de prueba
def test_crear_usuario():
    # JSON para el usuario
    usuario = {
        "username": "test1",
        "password": "test1",
        "nombre": "test1",
        "apellido": "string",
        "direccion": "string",
        "telefono": "string",
        "correo": "test1@test.com",
        "creacion": "2022-08-30T18:16:07.232490"
    }
    ###############
    # Identificar metodo
    print("######################################")
    print("funcion: {}".format("test_crear_usuario"))
    ###############
    # Realizar login
    response_token = cliente.post('/login/',data=usuario_login)
    ###############
    # Casos de afirmación: La salida debe dar usuario autenticado status.HTTP_200_OK
    assert response_token.status_code == 200
    assert response_token.json()["token_type"] == "bearer"
    # print(usuario_login)
    headers = {
        "Authorization":f"Bearer {response_token.json()['access_token']}"
    }
    response = cliente.post('/user/',json=usuario,headers=headers)

    ###############
    # Casos de afirmación: La salida debe dar usuario creado: HTTP_201_CREATED = 201
    assert response.status_code == 201
    ###############
    # Casos de afirmación: El mensaje al crear el usuario debe ser el configurado en el método del API (2 opciones)
    assert response.json() == {'respuesta':'Usuario creado satisfactoriamente'}
    assert response.json()["respuesta"] == 'Usuario creado satisfactoriamente'
    ###############
    # Print debug
    # print(response,dir(response),'status=',response.status_code)
    print(response.json())

def test_obtener_usuarios():
    ###############
    # Identificar metodo
    print("######################################")    
    print("funcion: {}".format("test_obtener_usuarios"))
    ###############
    # Realizar login
    response_token = cliente.post('/login/',data=usuario_login)
    ###############
    # Casos de afirmación: La salida debe dar usuario autenticado status.HTTP_200_OK
    assert response_token.status_code == 200
    assert response_token.json()["token_type"] == "bearer"
    # print(usuario_login)
    headers = {
        "Authorization":f"Bearer {response_token.json()['access_token']}"
    }
    response = cliente.get('/user/',headers=headers)
    ###############
    # Casos de afirmación: Deben de existir 2 usuarios creados
    assert len(response.json()) == 2
    ###############
    # Print debug
    # print(response,dir(response),'status=',response.status_code)
    print(response.json())

def test_obtener_usuario():
    id=1
    ###############
    # Identificar metodo
    print("######################################")
    print("funcion: {}".format("test_obtener_usuario id={}".format(id)))
    ###############
    # Realizar login
    response_token = cliente.post('/login/',data=usuario_login)
    ###############
    # Casos de afirmación: La salida debe dar usuario autenticado status.HTTP_200_OK
    assert response_token.status_code == 200
    assert response_token.json()["token_type"] == "bearer"
    # print(usuario_login)
    headers = {
        "Authorization":f"Bearer {response_token.json()['access_token']}"
    }
    response = cliente.post(f"/user/{id}",headers=headers)
    ###############
    # Casos de afirmación: Deben de existir 1 usuarios obtenido
    assert response.json()["username"] == "andres"
    ###############
    # Print debug
    # print(response,dir(response),'status=',response.status_code)
    print(response.json())

def test_eliminar_usuario():
    id=2
    ###############
    # Identificar metodo
    print("######################################")
    print("funcion: {}".format("test_eliminar_usuario id={}".format(id)))
    ###############
    # Realizar login
    response_token = cliente.post('/login/',data=usuario_login)
    ###############
    # Casos de afirmación: La salida debe dar usuario autenticado status.HTTP_200_OK
    assert response_token.status_code == 200
    assert response_token.json()["token_type"] == "bearer"
    # print(usuario_login)
    headers = {
        "Authorization":f"Bearer {response_token.json()['access_token']}"
    }
    response = cliente.delete(f"/user/{id}",headers=headers)
    response_user = cliente.post(f"/user/{id}",headers=headers)    
    ###############
    # Casos de afirmación: Deben de existir 1 usuarios obtenido
    assert response.json()["respuesta"] == "Usuario eliminado correctamente"
    assert response_user.json()["detail"] == "No existe el usuario con el id: {}".format(id)
    ###############
    # Print debug
    # print(response,dir(response),'status=',response.status_code)
    print(response.json())
    print(response_user.json())

def test_actualizar_usuario():
    id=1
    # JSON para el usuario
    usuario = {
        "username": "actualizar_usuario"
    }
    ###############
    # Identificar metodo
    print("######################################")
    print("funcion: {}".format("test_actualizar_usuario id={}".format(id)))
    ###############
    # Realizar login
    response_token = cliente.post('/login/',data=usuario_login)
    ###############
    # Casos de afirmación: La salida debe dar usuario autenticado status.HTTP_200_OK
    assert response_token.status_code == 200
    assert response_token.json()["token_type"] == "bearer"
    # print(usuario_login)
    headers = {
        "Authorization":f"Bearer {response_token.json()['access_token']}"
    }
    response = cliente.patch(f"/user/{id}",json=usuario,headers=headers)
    response_user = cliente.post(f"/user/{id}",headers=headers)    
    ###############
    # Casos de afirmación: Deben de existir 1 usuarios obtenido
    assert response.json()["respuesta"] == "Usuario actualizado correctamente"
    assert response_user.json()["username"] == usuario["username"]
    ###############
    # Print debug
    # print(response,dir(response),'status=',response.status_code)
    print(response.json())
    print(response_user.json())

def test_delete_database():
    # Identificar metodo
    print("######################################")
    print("funcion: {}".format("test_delete_database"))
    db_path = os.path.join(os.path.dirname(__file__),'test.db')
    os.remove(db_path)
    if os.path.exists(db_path):
        print ("Base de datos SQLite no pudo ser borrada")
    else:
        print("Base de datos SQLite borrada")     
    