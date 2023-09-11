from sqlmodel import create_engine


def obter_engine():
  # db_url = 'sqlite:///database.db'
  # db_url = 'postgresql+psycopg2://smarthome_b2hz_user:pmtszsfMU1fKevP6GYrznZdvJHxX2007@dpg-cjsd4rktjf3s73biv9tg-a.oregon-postgres.render.com/smarthome_b2hz'
  db_url = 'postgresql+psycopg2://postgres:postgres@localhost:5432/smarthome'
  engine = create_engine(db_url, echo=True)
  
  return engine
