from typing import List

from fastapi import APIRouter, Form, File, UploadFile, Depends
from starlette.background import BackgroundTasks
from starlette.requests import Request
from starlette.responses import HTMLResponse, StreamingResponse
from starlette.templating import Jinja2Templates

from users.db import UserModel
from users.models import User
from users.users import current_active_user
from video.models import Video
from video.schemas import GetListVideo
from video.services import save_video, open_file

video_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@video_router.post("/")
async def create_video(
        title: str = Form(...),
        description: str = Form(...),
        file: UploadFile = File(...),
        user: UserModel = Depends(current_active_user)
):
    return await save_video(user, file, title, description)


@video_router.get("/user/{user_pk}", response_model=List[GetListVideo])
async def get_list_video(user_pk: int):
    video_list = await Video.objects.filter(user=user_pk).all()
    return video_list


@video_router.get("/index/{video_pk}", response_class=HTMLResponse)
async def get_video(request: Request, video_pk: int):
    return templates.TemplateResponse("index.html", {"request": request, "path": video_pk})


@video_router.get("/video/{video_pk}")
async def get_streaming_video(request: Request, video_pk: int) -> StreamingResponse:
    file, status_code, content_length, headers = await open_file(request, video_pk)
    response = StreamingResponse(
        file,
        media_type='video/mp4',
        status_code=status_code
    )

    response.headers.update({
        'Accept-Ranges': 'bytes',
        'Content-Length': str(content_length),
        **headers
    })
    return response
