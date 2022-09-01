# Crear proyecto de migración alembic (Si se realiza desde cero, para el proyecto las configuraciones ya fueron realizadas)

alembic init migrations

Se crea el archivo alembic.ini    
Eliminar del alembic.ini, el contenido de la variable de conexión de base de datos sqlalchemy.url = xxx
se configura el migrations/env.py para asignar la conexión sqlalchemy.url = xxx

### migrations/env.py
from core.config import settings
### Cargar las variables de entorno
config.set_main_option('sqlalchemy.url',settings.DATABASE_URL)

### add your model's MetaData object here
- for 'autogenerate' support
- from app.db.models import Base
- target_metadata = Base.metadata
- target_metadata = None