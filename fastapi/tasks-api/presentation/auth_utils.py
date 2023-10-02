from jose import JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import infrastructure.jwt_provider as jwt_provider
from persistence.auth_repository import AuthRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/signin')


def get_logged_user(token: str = Depends(oauth2_scheme), repo: AuthRepository = Depends(AuthRepository)):

    try:
        payload = jwt_provider.decode(token)
        user_id = payload.get('id')
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token inválido!'
        )

    user = repo.get_user_by_id(user_id)

    return user.to_user_read()
