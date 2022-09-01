import os
from dotenv import load_dotenv
from pathlib import Path

env_path= Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str="Proyecto FastAPI"
    PROJECT_VERSION:str="1.0"
    CONN_POSTGRES_HOST:str=os.getenv('CONN_POSTGRES_HOST','')
    CONN_POSTGRES_USER:str=os.getenv('CONN_POSTGRES_USER','')
    CONN_POSTGRES_PASSWORD:str=os.getenv('CONN_POSTGRES_PASSWORD','')
    CONN_POSTGRES_PORT:int=os.getenv('CONN_POSTGRES_PORT','')
    CONN_POSTGRES_DB:str=os.getenv('CONN_POSTGRES_DB','')
    DATABASE_URL='postgresql://{}:{}@{}:{}/{}'.format(CONN_POSTGRES_USER,CONN_POSTGRES_PASSWORD,CONN_POSTGRES_HOST,CONN_POSTGRES_PORT,CONN_POSTGRES_DB)

settings = Settings()

