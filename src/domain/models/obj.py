from typing import Optional
from pydantic import BaseModel

from .creator_base import CreatorBaseSchema
from .binary import BinarySchema
from .tag import OutTagSchema


class BaseObjSchema(BaseModel):
    title: str
    description: Optional[str] = None
    binary_id: Optional[int] = None


class ObjSchema(BaseObjSchema, CreatorBaseSchema):
    pass


class OutObjSchema(ObjSchema):
    id: int


class FullObjSchema(OutObjSchema):
    binary: BinarySchema 
    tags: list[OutTagSchema]


class ObjCreationSchema(BaseObjSchema):
    user_id: int
    tags_id: list[int]
