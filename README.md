# Descripción del API

- Api de ejemplo, la cual se conecta a la base de datos postgres y por medio de un usuario/password hace login en el swagger.
- Por medio de pytest se realizan pruebas en una base de datos aparte SQLite
- Por medio de coverage se ejecutan las pruebas de pytest, obteniendo los resultados en un reporte HTML

# Descripción de los archivos
    .
    |-- arm/                            # Definición Continuous Deployment CD en Azure DevOps
    |   |-- scripts/                    # Comandos para Deployment
    |   |-- templates/                  # Plantillas ARM - Azure Resource Manager en formato JSON
    |-- app/                            # Carpeta principal del API
    |   |-- common/                     # Librerias/Clases/Funciones/Constantes/Mensajes de plataforma
    |   |   |-- hashig.py               # Funciones para encriptación con métodos hash
    |   |   |-- oauth.py                # Funciones para interactuar con métodos oauth
    |   |   |-- jwt.py                  # Funciones para interactuar con el estándard JWT (JSON Web Token)
    |   |-- core/                       # Definición de configuraciones base
    |   |   |-- config.py               # Definición de variables de ambiente como carga de variables de ambientes
    |   |-- db/                         # Definición conexiones a bases de datos y modelos - (Simil .Net DAL Data Access Layer)
    |   |   |-- conn_postgres.py        # Clase para conectar a la base de datos y su motor respectivo
    |   |   |-- models.py               # Definición de modelos de base de datos para interactuar con el ORM (Object Relational Mapping)
    |   |   |-- querys.py               # Querys de consulta a base de datos
    |   |-- repository/                 # Layer Controlador/Logica del negocio - (Simil .Net BLL / Business Logic sin conexión a Datos)
    |   |   |-- auth.py                 # Reglas de autenticación
    |   |   |-- user.py                 # Reglas para interactuar con las conexiones de las bases de datos
    |   |-- routers/                    # Definición Vistas / Enrutamiento a métodos get/post (Capa de controladores - Expuesta al cliente por postman)
    |   |   |-- auth.py                 # Vista/Métodos para interactuar con la autenticación / Login al API
    |   |   |-- user.py                 # Vista/Métodos para interactuar con la administración de usuarios en la base de datos
    |   |-- schemas/                    # Definiciones response_model
    |   |   |-- jwt.py                  # response_model para JWT (JSON Web Token)
    |   |   |-- user.py                 # response_model para interactuar con las vistas de usuario y la modificación de los atributos en la base de datos
    |   |-- migrations/                 # Carpeta de alembic para migraciones de base de datos (Autogenerada)
    |-- main.py                         # Código de inicio para el API
    |-- entrypoint.sh                   # Definición del ejecutable que usará el contenedor
    |-- requirements.txt                # Definición de paquetes Python requeridos
    |-- alembic.ini                     # lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python
    |-- user_create_init.py             # Método para crear el primer usuario para poder autenticarse al api por swagger
    |-- .env                            # Variables de entorno
    |-- Dockerfile                      # Instrucciones para construir contenedor
    |-- cd-pipeline-dev.yml             # manifiesto Continuous integration CI para Build/Compilar ambiente develop en Azure DevOps
    |-- cd-pipeline-prod.yml            # manifiesto Continuous integration CI para Build/Compilar ambiente production en Azure DevOps

# Preparar ambiente

### Activar entorno virtual
pipenv install

### Correr entorno virtual
pipenv shell

### Instalar requerimientos
pip install -r requirements.txt
pipenv graph

## Alistar la base de datos inicialmente
Configurar las variables de entorno para la base de datos .env obtener el nombre de la base de datos
Para el ejemplo tenemos un motor postgres instalado en localhost
CONN_POSTGRES_DB='fastapi_database'
Ejecutar en postgres: create database fastapi_database;

### Preparar alembic para crear todas las tablas e inicializar las versiones db.create_all()
alembic stamp head

### Crear/actualizar estructura de modelos y dejar un mensaje de commit
alembic revision --autogenerate -m "Inicializar modelos"

### Actualizar estructura existente en la base de datos (Agregar/Editar objetos)
alembic upgrade heads

### Crear usuario inicial para login
python user_create_init.py

# Ya se puede iniciar el Api
python main.py
Ingresar por: http://localhost:8000/docs
Login (Autorize) admin:password

![Alt text](/fotos/Screenshot_1.png?raw=true)

# Comando para realizar pruebas, no se necesita que esté corriendo el API
pytest -s # -s es para imprimir las salidas de la funcion print

# Coverage
### https://coverage.readthedocs.io/en/6.4.4/
Coverage.py es una herramienta para medir la cobertura de código de los programas de Python.
Supervisa su programa, anotando qué partes del código se han ejecutado, luego analiza la fuente para identificar el código que podría haberse ejecutado pero no se ejecutó.
La medición de cobertura se usa típicamente para medir la efectividad de las pruebas.
Puede mostrar qué partes de su código están siendo ejercitadas por pruebas y cuáles no.

## Comando
coverage run -m pytest
se crea el archivo .coverage

## Generar coverage en html
coverage html

Revisar resultados en la carpeta htmlcov