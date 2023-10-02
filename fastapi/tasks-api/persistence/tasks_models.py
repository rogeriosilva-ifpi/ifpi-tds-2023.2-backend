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

    def to_user_read(self):
        user = UserRead(id=self.id, name=self.name, login=self.login)
        return user


class UserRead(UserBase):
    id: str


class TaskBase(SQLModel):
    description: str = Field(min_length=3)
    done: bool = Field(default=False)


class TaskCreate(TaskBase):
    pass


class Task(TaskBase, table=True):
    id: str = Field(default=ulid(), primary_key=True)
    user_id: str | None = Field(default=None, foreign_key="user.id")

    @staticmethod
    def from_task_create(task_create: TaskCreate):
        task = Task()
        task.description = task_create.description
        task.done = task_create.done
        return task

    def to_task_read(self):
        task = TaskRead(
            id=self.id, description=self.description, done=self.done)
        return task


class TaskRead(TaskBase):
    id: str
    owner: UserRead | None = None
