from typing import Any, Generic

from src.application.interactor import Interactor, InputDTO, OutputDTO
from .repo_binded_app import RepoBindedApp


class DirectPassCreate(
    RepoBindedApp,
    Interactor[InputDTO, OutputDTO],
    Generic[InputDTO, OutputDTO],
):
    async def prepare_for_store(self, data: 'InputDTO') -> Any:
        return data

    async def __call__(self, data: 'InputDTO'):
        prepared_data = await self.prepare_for_store(data)
        return await self.repo.add(prepared_data)
