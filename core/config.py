#Archivo que nos permite conectarnos a la base de datos
from pydantic import BaseSettings #Nos permite hacer configuraciones
from typing import Optional #Nos permite manejar tipos de datos
from functools import lru_cache #Para que nos cree una instancia de la configuración cada vez que la llamemos

class Settings(BaseSettings):
    DATABASE_USERNAME: str = 'postgres'
    DATABASE_PASSWORD: str = '2019114020'
    DATABASE_HOST: str = 'localhost'
    DATABASE_NAME: str = 'mydb'

    DATABASE_URI: str = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:5433/{DATABASE_NAME}"

    class Config:
        case_sensitive: bool = True

@lru_cache 
def get_settings() -> Settings:
    return Settings()

settings = get_settings() #PARA HACER UN CACHÉ Y NO TENER QUE HACERLO TODO EL TIEMPO