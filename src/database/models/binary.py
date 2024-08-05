from typing import TypeAlias
import sqlalchemy as sa

from .creatore_base import CreatorBaseModel


class Binary(CreatorBaseModel):
    id = sa.Column(sa.BigInteger, primary_key=True)
    path = sa.Column(sa.String(1046))
    content_type = sa.Column(sa.String(256))
    size = sa.Column(sa.Integer)


BinaryModel: TypeAlias = Binary
