from typing import TypeAlias

from pydantic import Field
from src.domain.models import OutObjSchema
from src.utils import schemas
from src.application.common import GetPage
from .repo_binded import RepoBindedApp


class GetObjPageDTO(schemas.PageRequireData):
    tags_id: list[int] = Field(default_factory=list)


class GetObjPage(
    RepoBindedApp,
    GetPage[GetObjPageDTO, OutObjSchema],
):
    DTO: TypeAlias = GetObjPageDTO 

    async def get_page_data(self, data: 'GetObjPageDTO'):
        return await self.repo.page_by_tags(
            page=data.page, 
            count=data.page_size,
            tags_id=data.tags_id,
        )
