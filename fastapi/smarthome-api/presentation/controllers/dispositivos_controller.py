from fastapi import APIRouter, HTTPException, status
from sqlmodel import Session, delete, select

from application.ambientes_service import AmbienteService
from persistence.utils import obter_engine
from presentation.viewmodels.models import *

router = APIRouter()
prefix = '/ambientes/{ambiente_id}/dispositivos'

engine = obter_engine()

ambiente_service = AmbienteService()


def buscar_dispositivo_por_id(id: int):
    session = Session(engine)
    instrucao = select(Dispositivo).where(Dispositivo.id == id)
    dispositivo = session.exec(instrucao).first()
    # para carregar relação "ambiente"
    dispositivo.ambiente
    session.close()
    return dispositivo


@router.get('/')
def obter_dispositivos(ambiente_id: int):
    ambiente_atual = ambiente_service.obter_ambiente_por_id(ambiente_id)

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


@router.get('/{dispositivo_id}', response_model=DispositivoComAmbiente)
def obter_dispositivo(ambiente_id: int, dispositivo_id: int):
    dispositivo = buscar_dispositivo_por_id(dispositivo_id)

    # Fail Fast
    if not dispositivo or dispositivo.ambiente_id != ambiente_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Dispositivo não encontrado')

    return dispositivo


@router.post('/')
def adicionar_dispositivo(ambiente_id: int, dispositivo: Dispositivo):
    ambiente = ambiente_service.obter_ambiente_por_id(ambiente_id)

    if not ambiente:
        raise HTTPException(status_code=404, detail='Ambiente não encontrado')
    
    dispositivo.ambiente_id = ambiente_id
    session = Session(engine)
    session.add(dispositivo)
    session.commit()
    session.refresh(dispositivo)
    session.close()

    return dispositivo


@router.delete('/{dispositivo_id}')
def remover_dispositivo(ambiente_id: int, dispositivo_id: int):
    ambiente = ambiente_service.obter_ambiente_por_id(ambiente_id)

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


@router.put('/{dispositivo_id}/mover/{destino_id}')
def mover_dispositivo(origem_id: int, dispositivo_id: int, destino_id: int):

    dispositivo = buscar_dispositivo_por_id(dispositivo_id)
    
    if not dispositivo:
        raise HTTPException(status_code=404, detail="Dispositivo não localizado!")

    ambiente_origem = ambiente_service.obter_ambiente_por_id(origem_id)
    ambiente_destino = ambiente_service.obter_ambiente_por_id(destino_id)

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
