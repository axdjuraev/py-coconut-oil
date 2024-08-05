from pydantic import BaseModel


class CreatorBaseSchema(BaseModel):
    created_by_id: int

    class Config:
        from_attributes = True
