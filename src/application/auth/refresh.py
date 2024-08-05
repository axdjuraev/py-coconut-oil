from typing import TypeAlias, Union

from pydantic import BaseModel
from src.application.exceptions import ApplicationError
from src.domain.models.auth import LoginSchema
from .base import BaseAuthApp


class RefreshDTO(BaseModel):
    token: str


class Refresh(BaseAuthApp[RefreshDTO, Union[LoginSchema, None]]):
    DTO: TypeAlias = RefreshDTO 
    BaseError = "Token is invalid!"

    async def __call__(self, data: 'RefreshDTO'):
        try:
            email = self.auth_system.get_token_data(data.token)
        except Exception:
            raise ApplicationError(details=self.BaseError)

        if await self.repo.get_by_email(email) is None:
            raise ApplicationError(details=self.BaseError)

        return LoginSchema(
            access_token=self.auth_system.create_access_token(email),
            refresh_token=self.auth_system.create_refresh_token(email),
        )
