from typing import TypeAlias, Union
from pydantic import BaseModel
from src.domain.models.auth import LoginSchema
from .base import BaseAuthApp


class LoginDTO(BaseModel):
    email: str
    password: str


class Login(BaseAuthApp[LoginDTO, Union[LoginSchema, None]],):
    DTO: TypeAlias = LoginDTO 

    async def __call__(self, data: 'DTO'):
        if (
            (user := await self.repo.get_by_email(data.email)) is None
            or not self.auth_system.varify_password(data.password, user.password_hash)
        ):
            return None

        return LoginSchema(
            access_token=self.auth_system.create_access_token(data.email),
            refresh_token=self.auth_system.create_refresh_token(data.email),
        )
