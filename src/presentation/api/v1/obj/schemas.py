from src.domain import models


class ObjCreationRequest(models.BaseObjSchema):
    tags_id: list[int]


class ObjCreationResponse(models.OutObjSchema):
    pass
