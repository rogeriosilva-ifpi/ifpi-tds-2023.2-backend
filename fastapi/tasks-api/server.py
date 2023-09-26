from fastapi import FastAPI
from persistence.tasks_models import *
from persistence.db_utils import create_tables
from presetation.auth_controller import prefix as auth_prefix, router as auth_router

app = FastAPI()

create_tables()

# Register controllers
app.include_router(auth_router, prefix=auth_prefix)


@app.get('/tasks')
def get_all_tasks():
    return []
