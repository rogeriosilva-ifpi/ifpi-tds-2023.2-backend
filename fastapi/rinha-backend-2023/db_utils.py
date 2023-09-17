from sqlmodel import Session, SQLModel, create_engine


def get_engine():
  return create_engine("sqlite:///database.db")


def init_create_tables():
  SQLModel.metadata.create_all(get_engine())



    