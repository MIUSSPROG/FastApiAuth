import databases
import sqlalchemy
import fastapi_users.db
from fastapi_users_db_ormar import OrmarBaseUserModel, OrmarUserDatabase

from db_config import MainMeta
from users.models import UserDB


class UserModel(OrmarBaseUserModel):
    class Meta(MainMeta):
        pass