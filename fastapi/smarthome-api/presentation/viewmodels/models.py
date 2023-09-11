
from sqlmodel import Field, Relationship, SQLModel


class AmbienteBase(SQLModel):
    descricao: str
    icone: str | None = Field(default='icone.png')


class Ambiente(AmbienteBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    
    dispositivos: list['Dispositivo'] = Relationship(back_populates='ambiente')


class AmbienteLeitura(AmbienteBase):
    id: int


class DispositivoBase(SQLModel):
    description: str
    icone: str | None = Field(default='icone.png')
    estado_conexao: bool | None = Field(default=True)
    status: bool | None = Field(default=False)

    ambiente_id: int | None = Field(default=None, foreign_key="ambiente.id")


class DispositivoComAmbiente(DispositivoBase):
    id: int
    ambiente: AmbienteLeitura | None = None


# Vai virar tabela (table=True)
class Dispositivo(DispositivoBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    ambiente: Ambiente | None = Relationship(back_populates='dispositivos')
