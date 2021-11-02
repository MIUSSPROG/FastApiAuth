from typing import List

from pydantic import BaseModel

from users.schemas import User


class FollowerCreate(BaseModel):
    user: str


class FollowerList(FollowerCreate):
    user: User
    subscriber: List[User]