from fastapi import APIRouter, HTTPException, status
from sqlmodel import Session, delete, select

from application.ambientes_service import AmbienteService
from persistence.utils import obter_engine
from presentation.viewmodels.models import *

engine = obter_engine()

router = APIRouter()
prefix = '/ambientes'

ambientes_service = AmbienteService()


@router.get('/', status_code=status.HTTP_200_OK, response_model=list[AmbienteLeitura])
async def obter_ambientes():
    return ambientes_service.obter_todos_ambientes()


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=AmbienteLeitura)
async def obter_ambiente(id: int):
    ambiente = ambientes_service.obter_ambiente_por_id(id)

    # Fail Fast
    if not ambiente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Ambiente não encontrado')
    
    return ambiente


@router.post('/', status_code=status.HTTP_201_CREATED)
def criar_ambiente(ambiente: Ambiente):
    return ambientes_service.criar_ambiente(ambiente)

@router.put('/{id}', status_code=status.HTTP_200_OK)
def atualizar_ambientes(id: int, ambiente: Ambiente):
    return ambientes_service.atualizar_ambiente(id, ambiente)
    

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def remover_ambiente(id: int):
    ambientes_service.remover_ambiente(id)