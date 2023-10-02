from fastapi import APIRouter, status, HTTPException, Depends
from persistence.tasks_models import UserCreate
from persistence.auth_repository import AuthRepository
import infrastructure.hash_provider as hash_provider
import infrastructure.jwt_provider as jwt_provider
from presentation.models import LoginData
from presentation.auth_utils import get_logged_user


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
def signin(login_data: LoginData):
    # verificar se usuário existe
    user_found = auth_repo.get_user_by_login(login_data.login)

    if not user_found:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Usuário e/ou senha incorretos!'
        )

    # verificar a senha
    valid = hash_provider.verify(login_data.password, user_found.password)

    if not valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Usuário e/ou senha incorretos!'
        )

    access_token = jwt_provider.generate(user_found.id)

    return {'access_token': access_token}


@router.get('/me')
def me(usuario_logado=Depends(get_logged_user)):
    return usuario_logado
