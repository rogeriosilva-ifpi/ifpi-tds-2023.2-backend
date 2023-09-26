from sqlmodel import SQLModel, Field
from ulid import ulid


class UserBase(SQLModel):
    login: str = Field(nullable=False, unique=True)
    name: str = Field(min_length=6)


class UserCreate(UserBase):
    password: str = Field(min_length=6)


class User(UserBase, table=True):
    id: str = Field(default=ulid(), primary_key=True)
    password: str

    @staticmethod
    def from_user_create(user_create: UserCreate):
        user = User()
        user.login = user_create.login
        user.name = user_create.name
        user.password = user_create.password
        return user


class UserRead(UserBase):
    id: str


class TaskBase(SQLModel):
    description: str = Field(min_length=3)
    done: bool = Field(default=False)


class Task(TaskBase, table=True):
    id: str = Field(default=ulid(), primary_key=True)

    user_id: str | None = Field(default=None, foreign_key="user.id")


class TaskRead(TaskBase):
    id: str
    owner: User | None = None
