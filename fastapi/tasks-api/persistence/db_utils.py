from sqlmodel import create_engine, SQLModel


def get_engine():
    url = 'sqlite:///database.db'
    return create_engine(url, echo=True)


def create_tables():
    SQLModel.metadata.create_all(get_engine())
