from typing import TypeAlias

from pydantic import BaseModel

from src.domain import models
from src.domain.models.tag import OutTagSchema, TagSchema
from src.application.common import DirectPassCreate
from .repo_binded import RepoBindedApp


class CreateTagDTO(BaseModel):
    user_id: int
    meta: models.BaseTagSchema


class CreateTag(
    RepoBindedApp,
    DirectPassCreate[CreateTagDTO, OutTagSchema],
):
    DTO: TypeAlias = CreateTagDTO 

    async def prepare_for_store(self, data: 'DTO'):
        return TagSchema(
            **data.meta.model_dump(),
            created_by_id=data.user_id,
        )
