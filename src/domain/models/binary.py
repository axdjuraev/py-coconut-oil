from pydantic import BaseModel
from .creator_base import CreatorBaseSchema


class BaseBinarySchema(BaseModel):
    path: str
    content_type: str

    class Config:
        from_attributes = True


class BinarySchema(BaseBinarySchema, CreatorBaseSchema):
    pass


class OutBinarySchema(BinarySchema):
    id: int
