from typing import Optional, Union, Dict

import ormar

from db_config import MainMeta
from users.models import UserModel


class Follower(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    user: Optional[Union[UserModel, Dict]] = ormar.ForeignKey(UserModel, related_name="user")
    subscriber: Optional[Union[UserModel, Dict]] = ormar.ForeignKey(UserModel, related_name="subscriber")