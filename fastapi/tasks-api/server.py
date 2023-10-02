from fastapi import FastAPI, Depends
from presentation.auth_utils import get_logged_user
from persistence.tasks_models import *
from persistence.db_utils import create_tables
from presentation.auth_controller import prefix as auth_prefix, router as auth_router
from presentation.task_controller import prefix as task_prefix, router as task_router

app = FastAPI()

create_tables()

# Register controllers
app.include_router(auth_router, prefix=auth_prefix)
app.include_router(task_router, prefix=task_prefix)
