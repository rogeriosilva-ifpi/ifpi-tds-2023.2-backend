from pydantic import BaseModel


class LoginData(BaseModel):
    login: str
    password: str
