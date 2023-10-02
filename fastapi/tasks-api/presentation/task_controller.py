from fastapi import APIRouter, Depends, status, HTTPException
from presentation.auth_utils import get_logged_user
from persistence.tasks_models import UserRead, TaskCreate, Task
from persistence.task_repository import TaskRepository

router = APIRouter()
prefix = '/tasks'


@router.get('/')
def get_all_tasks(repo: TaskRepository = Depends(TaskRepository), logged_user: UserRead = Depends(get_logged_user)):
    return repo.get_all_by_user(logged_user)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_task(task_create: TaskCreate, repo: TaskRepository = Depends(TaskRepository), logged_user: UserRead = Depends(get_logged_user)):
    task = Task.from_task_create(task_create)
    task.user_id = logged_user.id

    created_task = repo.save(task)
    return created_task


@router.get('/{id}')
def detail_task(id: str, repo: TaskRepository = Depends(TaskRepository), logged_user: UserRead = Depends(get_logged_user)):
    task = repo.get_by_id(id)

    if not task or task.user_id != logged_user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found!")

    return task.to_task_read()
