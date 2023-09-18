from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, Response, status

from people_models import PersonCreate, PersonRead
from person_repository import PersonRepository

router = APIRouter()
prefix = '/pessoas'

@router.post('/', response_model=PersonRead)
def create_person(person: PersonCreate, response: Response, repo: PersonRepository = Depends(PersonRepository)):
  try:
    created_person = repo.save(person.toPerson())
    # response.headers['Location'] = f'/pessoas/{created_person.id}/'
    return created_person
  except Exception as e:
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Não foi possível criar a pessoa!')


@router.get('/{id}', response_model=PersonRead)
def get_person(id: str, repo: PersonRepository = Depends(PersonRepository)):
  person = repo.getOne(id)

  if not person:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Pessoa não encontrada!')

  return person


@router.get('/')
def get_people(t: Annotated[str, Query(min_length=1)], repo: PersonRepository = Depends(PersonRepository)):
  return repo.find(t)


