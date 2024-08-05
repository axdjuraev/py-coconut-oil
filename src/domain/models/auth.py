from pydantic import BaseModel


class LoginSchema(BaseModel):
    access_token: str
    refresh_token: str
