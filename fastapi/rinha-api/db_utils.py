from sqlmodel import create_engine, SQLModel
from decouple import config


def obter_engine():
    HOST = config('DB_HOST')
    PORT = config('DB_PORT')
    DB = config('DB_DATABASE')
    USER = config('DB_USER')
    PASSWORD = config('DB_PASSWORD')
    url_db = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    engine = create_engine(url_db, echo=True)
    return engine


def criar_tabelas():
    engine = obter_engine()
    SQLModel.metadata.create_all(engine)
