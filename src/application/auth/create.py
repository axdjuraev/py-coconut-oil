from typing import TypeAlias

from src.application.exceptions import ApplicationError
from src.domain.models import BaseUsersSchema
from .base import BaseAuthApp


class CreateAuthDTO(BaseUsersSchema):
    password: str


class CreateAuth(BaseAuthApp[CreateAuthDTO, None]):
    DTO: TypeAlias = CreateAuthDTO 

    async def __call__(self, data: 'DTO'):
        if await self.repo.get_by_login(data.email, data.username) is not None:
            raise ApplicationError(details=f"User already exists")

        password_hash = self.auth_system.get_password_hash(data.password)
        
        await self.repo.add(
            self.repo.Schema(
                **data.model_dump(),
                password_hash=password_hash,
            )
        )
