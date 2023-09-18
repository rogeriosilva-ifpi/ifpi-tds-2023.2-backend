from decouple import config
from sqlmodel import Session, SQLModel, create_engine


def get_engine():
  # Obter Usuário e senha de arquivo (.env)
  user = config('PG_USER')
  password = config('PG_PASSWORD')
  host = config('PG_HOST', 'localhost')
  port = config('PG_PORT', 5431)
  db = config('PG_DATABASE', 'rinha')

  # return create_engine("sqlite:///database.db")
  return create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}')


def init_create_tables():
  SQLModel.metadata.create_all(get_engine())



    