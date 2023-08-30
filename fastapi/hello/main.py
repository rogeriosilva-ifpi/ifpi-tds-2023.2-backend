from ast import List

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

proximo_id = 3

class Animal(BaseModel):
    id: int | None = None
    nome: str
    ano_nascimento: int
    cor: str

a1 = Animal(id=1, nome='Rabito', ano_nascimento=2012, cor='Branco')
b1 = Animal(id=2, nome='Pipoca', ano_nascimento=2015, cor='Cinza Mesclado')

animais = [a1, b1]

def buscar_animal_por_id(id: int):
    for animal in animais:
        if animal.id == id:
            return animal
    
    return None

@app.get('/hello')
def hello():
    return {"mensagem": "Olá seja bem-vindo!"}


@app.get('/animais', response_model=list[Animal])
def obter_todos_os_animais():
    return animais


@app.get('/animais/{id}')
def obter_um_animal(id: int):
    animal = buscar_animal_por_id(id)

    if animal == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail='Animal não localizado')

    return animal


@app.delete('/animais/{id}', status_code=status.HTTP_204_NO_CONTENT)
def remover_um_animal(id: int):
    animal = buscar_animal_por_id(id)

    if not animal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail='Animal não localizado')

    # remover da lista
    animais.remove(animal)


@app.post('/animais', status_code=status.HTTP_201_CREATED)
def novo_animal(animal: Animal):
    global proximo_id
    animal.id = proximo_id
    proximo_id += 1
    animais.append(animal)
    return animal
