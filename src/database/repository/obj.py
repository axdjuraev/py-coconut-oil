from typing import Iterable

import sqlalchemy as sa
from src.domain.models import ObjSchema as Schema
from src.domain.models import OutObjSchema as OutSchema
from src.database.models import ObjModel as Model
from src.database import models
from .base import BaseRepository


class ObjRepository(BaseRepository[Model, Schema, OutSchema]):
    async def page_by_tags(self, *args, tags_id: Iterable[int] = (), **kwargs):
        filters = []

        if tags_id:
            filters.append(models.ObjTagsModel.tag_id.in_(tags_id))

        return await self.all(
            *args, 
            query=(
                self._base_all_query
                .join(
                    models.ObjTagsModel, 
                    onclause=models.ObjTagsModel.obj_id == self.Model.id
                ).where(sa.and_(*filters))
            ),
            **kwargs,
        )
