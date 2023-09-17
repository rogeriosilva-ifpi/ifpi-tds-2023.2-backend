from inspect import stack
from operator import or_

from sqlalchemy import or_
from sqlmodel import Session, select

from db_utils import get_engine
from people_models import Person, PersonRead


class PersonRepository():

  def __init__(self) -> None:
    self.session = Session(get_engine())

  def save(self, person: Person) -> PersonRead:
    self.session.add(person)
    self.session.commit()
    return PersonRead.fromPerson(person)
  
  def getOne(self, id: str) -> PersonRead | None:
    person = self.session.get(Person, id)
    
    if person:
      return PersonRead.fromPerson(person)
    
    return None
  
  def find(self, t: str) -> list[PersonRead]:
    pattern = f'%{t}%'
    criteria = Person.nome.like(pattern) | Person.apelido.like(pattern) | Person.stack.like(pattern)
    people = self.session.query(Person).filter(criteria).limit(50)
    return list(map(PersonRead.fromPerson, people))
  
  
  def findBy(self, *, apelido: str) -> Person | None:
    sttm = select(Person).where(Person.apelido == apelido)
    return self.session.exec(sttm).first()
  
  def count(self) -> int:
    return self.session.query(Person).count()