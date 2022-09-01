from app.common.hashing import HashCrypt
from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# crear_usuario("admin","password")
# print(settings.DATABASE_URL)
engine_test = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine_test,autocommit=False,autoflush=False)

def insertar_usuario_prueba(usuario,password):
    try:
        password_hash = HashCrypt.EncryptPassword(password)
        engine_test.execute(
            f"""
            INSERT INTO usuario(username,password,nombre,apellido,direccion,telefono,correo)
            values
            ('{usuario}','{password_hash}','{usuario}','{usuario}','{usuario}','{usuario}','{usuario}@{usuario}')
            """
        )
        print(f"Usuario {usuario} creado satisfactoriamente")
    except Exception as e:
        print(f"Error creando usuario {usuario} debido a: {e}")


insertar_usuario_prueba("admin","password")

