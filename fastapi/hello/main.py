from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Animal(BaseModel):
    nome: str
    ano_nascimento: int
    cor: str

a1 = Animal(nome='Rabito', ano_nascimento=2012, cor='Branco')
b1 = Animal(nome='Pipoca', ano_nascimento=2015, cor='Cinza Mesclado')

animais = [a1, b1]

@app.get('/hello')
def hello():
    return {"mensagem": "Olá seja bem-vindo!"}


@app.get('/animais')
def obter_animais():
    return animais

@app.post('/animais')
def novo_animal(animal: Animal):
    animais.append(animal)
    return None
