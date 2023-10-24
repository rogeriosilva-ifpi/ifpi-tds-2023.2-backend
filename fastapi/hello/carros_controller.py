
from fastapi import APIRouter, FastAPI

router = APIRouter()
prefix = '/cars'


@router.get('/')
def get_all_cars():
    return []
