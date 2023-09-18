from fastapi import FastAPI
from pessoa_controller import router, prefix
from models import *
from db_utils import criar_tabelas

app = FastAPI()
criar_tabelas()


@app.get('/ping')
def ping():
    return 'Pong'


# registrar roteadores
app.include_router(router, prefix=prefix)
