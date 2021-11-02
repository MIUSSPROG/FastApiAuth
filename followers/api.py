from fastapi import APIRouter, Depends

from users.models import UserModel
from users.users import current_active_user
from . import schemas, models

follower_router = APIRouter(prefix='/followers', tags=["followers"])


@follower_router.post('/', response_model=schemas.FollowerCreate)
async def add_follower(
        schema: schemas.FollowerCreate,
        user: UserModel = Depends(current_active_user)
):
    host = await UserModel.objects.get(id=schema.user)
    return await models.Follower.objects.create(subscriber=user.dict(), user=host.dict())
