import datetime
from typing import Union, Optional

import ormar
from db_config import MainMeta
from users.db import UserModel
from users.models import UserDB


class Video(ormar.Model):
    class Meta(MainMeta):
        pass

    id = ormar.Integer(primary_key=True)
    title = ormar.String(max_length=50)
    description = ormar.String(max_length=500)
    file = ormar.String(max_length=1000)
    create_at = ormar.DateTime(default=datetime.datetime.now())
    # user: Union[UserModel, int, None] = ormar.ForeignKey(UserModel)
    user: Optional[UserModel] = ormar.ForeignKey(UserModel)