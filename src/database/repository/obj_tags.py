import sqlalchemy as sa
from src.domain.models import ObjTagSchema as Schema
from src.domain.models import OutObjTagSchema as OutSchema
from src.database.models import ObjTagsModel as Model
from .base import BaseRepository


class ObjTagsRepository(BaseRepository[Model, Schema, OutSchema]):
    async def add_all_by_obj_id(self, obj_id: int, tags_id: list[int]) -> None:
        data = [
            self.Model(
                obj_id=obj_id,
                tag_id=tag_id,
            )
            for tag_id in tags_id
        ]
        self.session.add_all(data)

    async def delete_all_by_obj_id(self, obj_id: int) -> None:
        await self.session.execute(
            sa.delete(self.Model)
            .where(self.Model.obj_id == obj_id)
        )
