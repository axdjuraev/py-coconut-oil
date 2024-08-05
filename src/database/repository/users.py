import sqlalchemy as sa
from src.domain.models import UsersSchema as Schema
from src.domain.models import OutUsersSchema as OutSchema
from src.database.models import UsersModel as Model
from .base import BaseRepository


class UsersRepository(BaseRepository[Model, Schema, OutSchema]):
    async def get_by_email(self, email):
        return await self.get(
            filters=(
                self.Model.email == email,
            )
        )

    async def get_by_login(self, email, username):
        return await self.get(
            filters=(
                sa.or_(
                    self.Model.email == email,
                    self.Model.username == username,
                ),
            )
        )
