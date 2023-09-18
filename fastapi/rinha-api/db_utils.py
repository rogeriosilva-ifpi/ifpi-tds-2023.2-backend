from sqlmodel import create_engine, SQLModel


def obter_engine():
    url_db = 'postgresql+psycopg2://docker:docker@localhost:5430/rinha_api'
    engine = create_engine(url_db, echo=True)
    return engine


def criar_tabelas():
    engine = obter_engine()
    SQLModel.metadata.create_all(engine)
