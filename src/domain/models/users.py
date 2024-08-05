from pydantic import BaseModel
from .base import BaseSchema


class BaseUsersSchema(BaseModel):
    email: str
    username: str

    class Config:
        from_attributes = True


class UsersSchema(BaseUsersSchema):
    password_hash: str


class OutUsersSchema(UsersSchema, BaseSchema):  # type: ignore
    id: int
