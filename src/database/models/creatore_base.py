import sqlalchemy as sa

from .base import BaseModel
from .users import UsersModel


class CreatorBaseModel(BaseModel):
    __abstract__ = True

    created_by_id = sa.Column(sa.ForeignKey(UsersModel.id))
