# Activar entorno virtual
pipenv install

# Correr entorno virtual
pipenv shell

# Instalar requerimientos
pip install -r requirements.txt
pipenv graph

# Correr uvicorn
# uvicorn main:app

python main.py

####################
# Crear proyecto de migración alembic
alembic init migrations
    # Crea las carpetas
    #  - alembic.ini
    #  + migrations
    #    + version
    #    - env.py
    #    - README
    #    - script.py.make

####################
# alembic.ini    
Eliminar del alembic.ini, el contenido de la variable de conexión de base de datos sqlalchemy.url = xxx
se configura el migrations/env.py para asignar la conexión sqlalchemy.url = xxx

####################
# migrations/env.py
from core.config import settings
##################
# Cargar las variables de entorno
config.set_main_option('sqlalchemy.url',settings.DATABASE_URL)

# add your model's MetaData object here
# for 'autogenerate' support
from app.db.models import Base
target_metadata = Base.metadata
# target_metadata = None

####################
# Realizar migraciones (Se realiza por cada cambio)

# Crear/actalizar estructura de modelos y dejar un mensaje de commit
alembic revision --autogenerate -m "Crear modelos"

# Actualizar estructura existente en la base de datos (Agregar/Editar objetos)
alembic upgrade heads

####################
# Realizar pruebas
# -s es para imprimir las salidas de la funcion print
pytest -s

####################
# Coverage
# https://coverage.readthedocs.io/en/6.4.4/
# Coverage.py es una herramienta para medir la cobertura de código de los programas de Python.
# Supervisa su programa, anotando qué partes del código se han ejecutado, luego analiza la fuente para identificar el código que podría haberse ejecutado pero no se ejecutó.
# La medición de cobertura se usa típicamente para medir la efectividad de las pruebas.
# Puede mostrar qué partes de su código están siendo ejercitadas por pruebas y cuáles no.

pip install coverage

coverage run -m pytest
# se crea el archivo .coverage

# leer coverage
coverage html

####################
# Git - Git ignore
# https://github.com/github/gitignore/blob/main/Python.gitignore