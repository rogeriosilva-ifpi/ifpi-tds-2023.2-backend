from sqlmodel import Session, select
from db_utils import obter_engine
from models import PessoaCreate, Pessoa


class PessoaRepository:

    def __init__(self):
        self.session = Session(obter_engine())

    def salvar(self, pessoa: PessoaCreate):
        nova_pessoa = Pessoa.from_pessoa_create(pessoa)

        self.session.add(nova_pessoa)
        self.session.commit()
        self.session.refresh(nova_pessoa)

        return nova_pessoa

    def obter_por_id(self, id: str):
        return self.session.get(Pessoa, id)

    def obter_por_apelido(self, apelido: str):
        sttm = select(Pessoa).where(Pessoa.apelido == apelido)
        return self.session.exec(sttm).first()
