from typing import TypeAlias
import sqlalchemy as sa

from .binary import BinaryModel
from .creatore_base import CreatorBaseModel


class Obj(CreatorBaseModel):
    id = sa.Column(sa.BigInteger, primary_key=True)
    title = sa.Column(sa.String(255))
    description = sa.Column(sa.String(255), nullable=True)
    binary_id = sa.Column(sa.ForeignKey(BinaryModel.id))


ObjModel: TypeAlias = Obj
