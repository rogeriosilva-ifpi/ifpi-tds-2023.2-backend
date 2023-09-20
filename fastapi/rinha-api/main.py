from fastapi import FastAPI, Request
from pessoa_controller import router, prefix
from models import *
from db_utils import criar_tabelas
from pessoa_repository import PessoaRepository

app = FastAPI()
criar_tabelas()


@app.get('/ping')
def ping():
    return 'Pong'


@app.get('/contagem-pessoas', response_model=int)
def contagem_pessoas():
    return PessoaRepository().contagem_pessoas()


# registrar roteadores
app.include_router(router, prefix=prefix)
