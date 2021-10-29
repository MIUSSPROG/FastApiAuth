from fastapi_users import models
from pydantic import EmailStr


class User(models.BaseUser):
    username: str


class UserCreate(models.CreateUpdateDictModel):
    username: str
    email: EmailStr
    password: str


class UserUpdate(models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass
