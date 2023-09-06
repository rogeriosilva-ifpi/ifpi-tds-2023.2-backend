from curses import noraw

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import table
from sqlmodel import (Field, Relationship, Session, SQLModel, create_engine,
                      delete, select, update)
from ulid import ulid

app = FastAPI()

# SQL Model
# db_url = 'sqlite:///database.db'
db_url = 'postgresql+psycopg2://postgres:postgres@localhost:5432/smarthome'
# db_url = 'postgresql+psycopg2://smarthome_b2hz_user:pmtszsfMU1fKevP6GYrznZdvJHxX2007@dpg-cjsd4rktjf3s73biv9tg-a.oregon-postgres.render.com/smarthome_b2hz'
# postgres://user:password@host/db

engine = create_engine(db_url, echo=True)


# Ativar CORS
origins = ['http://localhost:5500',
           'http://127.0.0.1:5500',
           'https://smarthome-web.onrender.com']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ambientes = []

ambiente_id = 0
dispositivo_id = 0


class Ambiente(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    descricao: str
    icone: str | None = Field(default='icone.png')
    dispositivos: list['Dispositivo'] = Relationship(back_populates='ambiente')


class Dispositivo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    description: str
    icone: str | None = Field(default='icone.png')
    estado_conexao: bool | None = Field(default=True)
    status: bool | None = Field(default=False)

    ambiente_id: int | None = Field(default=None, foreign_key="ambiente.id")
    ambiente: Ambiente | None = Relationship(back_populates='dispositivos')




SQLModel.metadata.create_all(engine)

'''Ambiente'''
def buscar_ambiente_por_id(id: int):
    session = Session(engine)
    instrucao = select(Ambiente).where(Ambiente.id == id)
    ambiente = session.exec(instrucao).first()
    session.close()
    return ambiente

@app.get('/ambientes', status_code=status.HTTP_200_OK)
def show_ambiente():
    session = Session(engine)
    instrucao = select(Ambiente)
    ambientes = session.exec(instrucao).fetchall()
    session.close()

    return ambientes

@app.post('/ambientes', status_code=status.HTTP_201_CREATED)
def criar_ambiente(ambiente: Ambiente):
    session = Session(engine)
    session.add(ambiente)
    session.commit()
    session.refresh(ambiente)
    session.close()
    return ambiente

@app.put('/ambientes/{id}', status_code=status.HTTP_200_OK)
def atualizar_ambientes(id: int, ambiente: Ambiente):
    ambiente_atual = buscar_ambiente_por_id(id)

    # Fail Fast
    if not ambiente_atual:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Ambiente não encontrado')
    
    ambiente_atual.descricao = ambiente.descricao
    session = Session(engine)
    session.add(ambiente_atual)
    session.commit()
    session.close()

    return ambiente_atual
    

@app.delete('/ambientes/{id}', status_code=status.HTTP_204_NO_CONTENT)
def remover_ambiente(id: int):
    ambiente = buscar_ambiente_por_id(id)
    
    if not ambiente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Ambiente não encontrado')
    
    # if len(ambiente.items) > 0:
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Ambiente não pode ser removido")
    
    session = Session(engine)
    instrucao = delete(Ambiente).where(Ambiente.id == id)
    session.exec(instrucao)
    session.commit()
    session.close()

'''Área Dispositivo'''

@app.get('/ambientes/{ambiente_id}/dispositivos')
def obter_dispositivos(ambiente_id: int):
    ambiente_atual = buscar_ambiente_por_id(ambiente_id)

    # Fail Fast
    if not ambiente_atual:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Ambiente não encontrado')

    # Buscar dispositivos
    session = Session(engine)
    inst = select(Dispositivo)\
        .where(Dispositivo.ambiente_id == ambiente_id)
    
    dispositivos = session.exec(inst).fetchall()
    session.close()
    return dispositivos


@app.post('/ambientes/{id}/dispositivos')
def adicionar_dispositivo(id: int, dispositivo: Dispositivo):
    ambiente = buscar_ambiente_por_id(id)

    if not ambiente:
        raise HTTPException(status_code=404, detail='Ambiente não encontrado')
    
    dispositivo.ambiente_id = id
    session = Session(engine)
    session.add(dispositivo)
    session.commit()
    session.refresh(dispositivo)
    session.close()

    return dispositivo


@app.delete('/ambientes/{ambiente_id}/dispositivos/{dispositivo_id}')
def remover_dispositivo(ambiente_id: int, dispositivo_id: int):
    ambiente = buscar_ambiente_por_id(ambiente_id)

    if not ambiente:
        raise HTTPException(status_code=404, detail='Ambiente não localizado!')


    dispositivo = buscar_dispositivo_por_id(dispositivo_id)

    if not dispositivo or dispositivo.ambiente_id != ambiente.id:
        raise HTTPException(status_code=404, detail='Dispositivo não localizado!')
    
    session = Session(engine)
    instrucao = delete(Dispositivo).where(Dispositivo.id == dispositivo_id)
    session.exec(instrucao)
    session.commit()
    session.close()


def buscar_dispositivo_por_id(id: int):
    session = Session(engine)
    instrucao = select(Dispositivo).where(Dispositivo.id == id)
    dispositivo = session.exec(instrucao).first()
    session.close()
    return dispositivo

@app.put('/ambientes/{origem_id}/dispositivos/{dispositivo_id}/mover/{destino_id}')
def mover_dispositivo(origem_id: int, dispositivo_id: int, destino_id: int):

    dispositivo = buscar_dispositivo_por_id(dispositivo_id)
    
    if not dispositivo:
        raise HTTPException(status_code=404, detail="Dispositivo não localizado!")

    ambiente_origem = buscar_ambiente_por_id(origem_id)
    ambiente_destino = buscar_ambiente_por_id(destino_id)

    if not ambiente_origem or not ambiente_destino:
        raise HTTPException(status_code=404, detail="Ambiente Origem/Destino não localizado!")
    
    if ambiente_origem.id == ambiente_destino.id:
        raise HTTPException(status_code=400, detail="Ambiente de destino deve diferente do de origem!")
    
    
    dispositivo.ambiente_id = ambiente_destino.id

    session = Session(engine)
    session.add(dispositivo)
    session.commit()
    session.close()

    return dispositivo
    
