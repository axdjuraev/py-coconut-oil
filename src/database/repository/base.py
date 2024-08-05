from typing import Generic, TypeVar

import sqlalchemy as sa
from axsqlalchemy.repository import BaseRepository as _BaseRepository
from axsqlalchemy.repository.types import BaseTableAt, TIModel, TOModel


class IDBaseTableAt(BaseTableAt):
    __abstract__ = True

    id = sa.Column(sa.Integer, primary_key=True)


TIDBaseTableAt = TypeVar('TIDBaseTableAt', bound=IDBaseTableAt)


class BaseRepository(
    _BaseRepository[TIDBaseTableAt, TIModel, TOModel],
    Generic[TIDBaseTableAt, TIModel, TOModel],
):
    __abstract__ = True

    async def add(self, obj: TIModel, autosave=True) -> TOModel:
        return await super().add(obj, autosave=autosave)

    async def all_non_existence_by_ids(self, ids):
        existence = {x.id: 1 for x in await self.all_by_ids(ids)}
        return [x for x in ids if x not in existence]

    async def all_by_ids(self, ids):
        return await self.all(
            filters=(
                self.Model.id.in_(ids),
            )
        )
