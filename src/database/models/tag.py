from typing import TypeAlias
import sqlalchemy as sa
from sqlalchemy.orm import relationship

from .creatore_base import CreatorBaseModel


class Tag(CreatorBaseModel):
    id = sa.Column(sa.BigInteger, primary_key=True)
    name = sa.Column(sa.String(1046))
    parent_id = sa.Column(sa.ForeignKey('tag.id'))

    sub_tags = relationship("Tag", cascade="all", remote_side=[parent_id], lazy='joined', back_populates="parent")
    parent = relationship("Tag", remote_side=[id], lazy='joined', back_populates="sub_tags")


TagModel: TypeAlias = Tag
