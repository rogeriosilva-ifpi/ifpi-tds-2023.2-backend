from curses import noraw

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ulid import ulid

app = FastAPI()

# Ativar CORS
origins = ['http://localhost:5500','https://smarthome-web.onrender.com']

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

class Dispositivo(BaseModel):
    id: str | None = None
    description: str
    icone: int | None
    estado_conexao: str | None
    status: bool | None

class Ambiente(BaseModel):
    id: str | None = None
    descricao: str
    icone: int | None = None
    items: list[Dispositivo] = []

'''Aréa Ambiente'''
def buscar_ambiente_por_id(id: str):
    for ambiente in ambientes:
        if ambiente.id == id:
            return ambiente
    return None

@app.get('/ambientes', status_code=status.HTTP_200_OK)
def show_ambiente():
    return ambientes

@app.post('/ambientes', status_code=status.HTTP_201_CREATED)
def criar_ambiente(ambiente: Ambiente):
    # global ambiente_id
    # ambiente.icone = ambiente_id
    # ambiente_id += 1
    ambiente.id = ulid()
    ambientes.append(ambiente)
    return ambiente

@app.put('/ambientes/{id}', status_code=status.HTTP_200_OK)
def atualizar_ambientes(id: str, ambiente: Ambiente):
    ambiente_atual = buscar_ambiente_por_id(id)

    # Fail Fast
    if not ambiente_atual:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Ambiente não encontrado')
    
    ambiente_atual.descricao = ambiente.descricao

    return ambiente_atual
    

@app.delete('/ambientes/{id}', status_code=status.HTTP_204_NO_CONTENT)
def remover_ambiente(id: str):
    ambiente = buscar_ambiente_por_id(id)
    
    if not ambiente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Ambiente não encontrado')
    
    if len(ambiente.items) > 0:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Ambiente não pode ser removido")
    
    ambientes.remove(ambiente)

'''Área Dispositivo'''
@app.post('/ambientes/{id}/dispositivos')
def adicionar_dispositivo(id: str, dispositivo: Dispositivo):
    ambiente = buscar_ambiente_por_id(id)

    if not ambiente:
        raise HTTPException(status_code=404, detail='Ambiente não encontrado')
    
    dispositivo.id = ulid()
    ambiente.items.append(dispositivo)
    return ambiente.items


@app.delete('/ambientes/{ambiente_id}/dispositivos/{dispositivo_id}')
def remover_dispositivo(ambiente_id: str, dispositivo_id: str):
    ambiente = buscar_ambiente_por_id(ambiente_id)

    if not ambiente:
        raise HTTPException(status_code=404, detail='Ambiente não localizado!')


    dispositivo = buscar_dispositivo_por_id(dispositivo_id, ambiente)

    if not dispositivo:
        raise HTTPException(status_code=404, detail='Dispositivo não localizado!')
    
    ambiente.items.remove(dispositivo)


def buscar_dispositivo_por_id(id, ambiente):
    for item in ambiente.items:
        if item.id == id:
            return item
    return None

@app.put('/ambientes/{origem_id}/dispositivos/{dispositivo_id}/mover/{destino_id}')
def mover_dispositivo(origem_id: str, dispositivo_id: str, destino_id: str):
    ambiente_origem = buscar_ambiente_por_id(origem_id)
    ambiente_destino = buscar_ambiente_por_id(destino_id)

    if not ambiente_origem or not ambiente_destino:
        raise HTTPException(status_code=404, detail="Ambiente Origem/Destino não localizado!")
    
    dispositivo = buscar_dispositivo_por_id(dispositivo_id, ambiente_origem)

    if not dispositivo:
        raise HTTPException(status_code=404, detail="Dispositivo não localizado!")

        
    ambiente_origem.items.remove(dispositivo)
    ambiente_destino.items.append(dispositivo)
    
