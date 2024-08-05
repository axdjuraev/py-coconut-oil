from typing import Optional
from .base import BaseSchema


class ObjTagSchema(BaseSchema):
    name: str
    parent_id: Optional[int] = None


class OutObjTagSchema(ObjTagSchema):
    id: int
