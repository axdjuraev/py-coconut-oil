from typing import Generic, TypeVar, Union

from pydantic import BaseModel
from src.application.interactor import Interactor, OutputDTO
from src.application.common.repo_binded_app import RepoBindedApp


class IDBindedDTO(BaseModel):
    id: int


TIDBindedDTO = TypeVar('TIDBindedDTO', bound=IDBindedDTO)


class GetByID(
    RepoBindedApp,
    Interactor[TIDBindedDTO, Union[OutputDTO, None]],
    Generic[TIDBindedDTO, OutputDTO],
):
    async def __call__(self, data: 'TIDBindedDTO'):
        return await self.repo.get(data.id)
