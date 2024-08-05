from typing import TypeAlias
import sqlalchemy as sa

from .base import BaseModel
from .obj import ObjModel
from .tag import TagModel


class ObjTags(BaseModel):
    id = sa.Column(sa.BigInteger, primary_key=True)
    obj_id = sa.Column(sa.ForeignKey(ObjModel.id))
    tag_id = sa.Column(sa.ForeignKey(TagModel.id))


sa.Index(
    'obj_tag_idx', 
    ObjTags.obj_id, 
    ObjTags.tag_id,
    unique=True,
)

ObjTagsModel: TypeAlias = ObjTags
