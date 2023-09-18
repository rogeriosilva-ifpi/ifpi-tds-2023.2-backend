from fastapi import APIRouter, status, HTTPException, Response
from models import PessoaCreate, Pessoa
from sqlmodel import Session
from db_utils import obter_engine
from pessoa_repository import PessoaRepository

router = APIRouter()
prefix = '/pessoas'

repo = PessoaRepository()


@router.post('/', status_code=status.HTTP_201_CREATED)
def adicionar_pessoa(pessoa: PessoaCreate, response: Response):
    pessoa_encontrada = repo.obter_por_apelido(pessoa.apelido)

    if pessoa_encontrada:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Apelido indisponível!')

    nova_pessoa = repo.salvar(pessoa)
    response.headers['Location'] = f'/pessoas/{nova_pessoa.id}'

    return nova_pessoa.id


@router.get('/{id}')
def obter_pessoa(id: str):
    pessoa = repo.obter_por_id(id)

    if not pessoa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Pessoa não localizada!')

    return pessoa.to_pessoa_read()
