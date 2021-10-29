from fastapi import APIRouter, Depends
from fastapi_users_db_ormar import OrmarUserDatabase

from users.models import UserModel
from users.users import fastapi_users, jwt_authentication, current_active_user
from users.schemas import UserDB

user_router = APIRouter()

user_router.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
)
user_router.include_router(
    fastapi_users.get_register_router(), prefix="/auth", tags=["auth"]
)
user_router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
user_router.include_router(
    fastapi_users.get_verify_router(),
    prefix="/auth",
    tags=["auth"],
)
user_router.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])


@user_router.get("/authenticated-route")
async def authenticated_route(user: UserDB = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}
