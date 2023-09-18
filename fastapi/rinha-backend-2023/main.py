from fastapi import Depends, FastAPI

from db_utils import init_create_tables
from people_controller import prefix, router
from person_repository import PersonRepository
from validation_middlewares import ValidateApelidoMiddleware

app = FastAPI()

app.include_router(router=router, prefix=prefix)

# app.add_middleware(ValidateApelidoMiddleware)

init_create_tables()

@app.get('/contagem-pessoas')
def count_people(repo: PersonRepository = Depends(PersonRepository)):
  return repo.count()


