from typing import Generic, TypeVar

from src.application.interactor import Interactor, OutputDTO
from src.utils import schemas
from src.utils.schemas import PageRequireData
from .repo_binded_app import RepoBindedApp


TPageRequireDTO = TypeVar('TPageRequireDTO', bound=PageRequireData)


class GetPage(
    RepoBindedApp,
    Interactor[TPageRequireDTO, schemas.Page[OutputDTO]],
    Generic[TPageRequireDTO, OutputDTO],
):
    async def get_total_size(self, _: 'TPageRequireDTO'):
        return await self.repo.all_count()

    async def get_page_data(self, data: 'TPageRequireDTO'):
        return await self.repo.all(page=data.page, count=data.page_size)

    async def __call__(self, data: 'TPageRequireDTO'):
        total_size = await self.get_total_size(data)
        page_data = await self.get_page_data(data)

        return schemas.Page(
            data=page_data,
            meta=schemas.PageMetadata(
                page=data.page,
                page_size=data.page_size,
                total_size=total_size,
            )
        )
