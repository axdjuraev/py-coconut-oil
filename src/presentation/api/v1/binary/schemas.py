from pydantic import BaseModel
from src.domain import models


class BinaryCreationRequest(models.BaseBinarySchema):
    pass


class BinaryCreationResponse(BaseModel):
    id: int
