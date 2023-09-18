from sqlmodel import SQLModel, Field
from datetime import date
from ulid import ulid


class PessoaBase(SQLModel):
    apelido: str = Field(nullable=False, max_length=32)
    nome: str = Field(nullable=False, max_length=100)
    nascimento: date


class PessoaCreate(PessoaBase):
    stack: list[str] | None = Field(default=[])


class PessoaRead(PessoaBase):
    id: str
    stack: list[str]


class Pessoa(PessoaBase, table=True):
    id: str = Field(default=ulid(), primary_key=True)
    stack: str

    @staticmethod
    def from_pessoa_create(pessoa_create: PessoaCreate):
        pessoa = Pessoa(nome=pessoa_create.nome,
                        apelido=pessoa_create.apelido,
                        nascimento=pessoa_create.nascimento,
                        stack=','.join(pessoa_create.stack))
        return pessoa

    def to_pessoa_read(self):
        pessoa_read = PessoaRead(id=self.id,
                                 nome=self.nome,
                                 apelido=self.apelido,
                                 nascimento=self.nascimento,
                                 stack=self.stack.split(','))
        return pessoa_read
