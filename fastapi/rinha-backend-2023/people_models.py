from datetime import date
from inspect import stack

from sqlmodel import Field, SQLModel
from ulid import ulid


class PersonBase(SQLModel):
  apelido: str = Field(unique=True, max_length=32, nullable=False)
  nome: str = Field(max_length=100, nullable=False)
  nascimento: date


class PersonRead(PersonBase):
  id: str
  stack: list[str]

  @staticmethod
  def fromPerson(person):
    stack = person.stack.split(',')
    del person.stack
    person_read = PersonRead(**person.__dict__, stack=stack)
    return person_read


class PersonCreate(PersonBase):
  stack: list[str] | None = Field(min_items=1, nullable=True)

  def toPerson(self):
    print(self.__dict__)
    person = Person(**self.__dict__)
    person.stack = ','.join(self.stack)
    return person


class Person(PersonBase, table=True):
  id: str = Field(default=ulid(), primary_key=True)
  stack: str

