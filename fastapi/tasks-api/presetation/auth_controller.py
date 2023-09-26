from fastapi import APIRouter, status, HTTPException
from persistence.tasks_models import UserCreate
from persistence.auth_repository import AuthRepository
import infrastructure.hash_provider as hash_provider
from presetation.models import LoginData


router = APIRouter()
prefix = '/auth'

auth_repo = AuthRepository()


@router.post('/signup', status_code=status.HTTP_201_CREATED)
def signup(user: UserCreate):

    user_found = auth_repo.get_user_by_login(user.login)

    if user_found:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Login já utilizado!')

    user.password = hash_provider.hash(user.password)
    user_created = auth_repo.save(user)
    return {'id': user_created.id}


@router.post('/signin', status_code=status.HTTP_200_OK)
def signin(input: LoginData):
    # verificar se usuário existe
    user_found = auth_repo.get_user_by_login(input.login)

    if not user_found:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Usuário e/ou senha incorretos!')

    # verificar a senha
    valid = hash_provider.verify(input.password, user_found.password)

    if not valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Usuário e/ou senha incorretos!')

    return {'access_token': 'My-Fake-JWT-Token-!@#$%ˆ&*()'}
