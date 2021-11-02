from fastapi import FastAPI
from fastapi_users_db_ormar import OrmarUserDatabase

from db_config import database, metadata, engine
from followers.api import follower_router
from users.api import user_router
from video.api import video_router

app = FastAPI()
app.state.database = database
metadata.create_all(engine)


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


app.include_router(video_router)
app.include_router(user_router)
app.include_router(follower_router)
