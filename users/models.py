import databases
import ormar
import sqlalchemy
import fastapi_users.db
from fastapi_users_db_ormar import OrmarBaseUserModel, OrmarUserDatabase

from db_config import MainMeta
from users.schemas import UserDB


class UserModel(OrmarBaseUserModel):
    class Meta(MainMeta):
        tablename = "users"

    username: str = ormar.String(max_length=100, unique=True)


def get_user_db():
    yield OrmarUserDatabase(UserDB, UserModel)