from fastapi import HTTPException, status
from sqlalchemy import delete
from sqlmodel import Session, delete, select

from persistence.utils import obter_engine
from presentation.viewmodels.models import *


class AmbienteService():

  def __init__(self):
    self.session = Session(obter_engine())

  def obter_todos_ambientes(self):
    instrucao = select(Ambiente)
    ambientes = self.session.exec(instrucao).fetchall()
    self.session.close()
    
    return ambientes

  def obter_ambiente_por_id(self, id: int):
    instrucao = select(Ambiente).where(Ambiente.id == id)
    ambiente = self.session.exec(instrucao).first()
    self.session.close()

    return ambiente
  
  def criar_ambiente(self, ambiente: Ambiente):
    self.session.add(ambiente)
    self.session.commit()
    self.session.refresh(ambiente)
    self.session.close()

    return ambiente

  def atualizar_ambiente(self, id: int, ambiente: Ambiente):
    ambiente_atual = self.obter_ambiente_por_id(id)

    # Fail Fast
    if not ambiente_atual:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Ambiente não encontrado')
    
    ambiente_atual.descricao = ambiente.descricao
    
    self.session.add(ambiente_atual)
    self.session.commit()
    self.session.close()

    return ambiente_atual
  
  def remover_ambiente(self, id: int):
    ambiente = self.obter_ambiente_por_id(id)
    
    if not ambiente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Ambiente não encontrado')
    
    instrucao = delete(Ambiente).where(Ambiente.id == id)
    self.session.exec(instrucao)
    self.session.commit()
    self.session.close()