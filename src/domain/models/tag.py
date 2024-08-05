from typing import Optional

from pydantic import BaseModel

from src.domain.models.base import BaseSchema
from .creator_base import CreatorBaseSchema


class BaseTagSchema(BaseModel):
    name: str
    parent_id: Optional[int] = None


class TagSchema(BaseTagSchema, CreatorBaseSchema):
    pass


class OutTagSchema(TagSchema, BaseSchema):
    id: int


class FullTagSchema(OutTagSchema):
    parent: Optional['FullTagSchema'] = None
