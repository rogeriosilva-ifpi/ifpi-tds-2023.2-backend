from sqlmodel import create_engine


def obter_engine():
  # db_url = 'sqlite:///database.db'
  db_url = 'postgresql+psycopg2://docker:docker@localhost:5430/smarthome'
  engine = create_engine(db_url, echo=True)
  
  return engine
