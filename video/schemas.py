from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str


class UploadVideo(BaseModel):
    title: str
    description: str
    # tags: List[str] = None


class GetListVideo(BaseModel):
    id: int
    title: str
    description: str


class GetVideo(GetListVideo):
    user: User


class Message(BaseModel):
    message: str