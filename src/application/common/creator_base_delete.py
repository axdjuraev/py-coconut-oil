from typing import Generic, TypeVar, Union
from pydantic import BaseModel

from src.application.interactor import Interactor, OutputDTO
from .repo_binded_app import RepoBindedApp
from .. import exceptions as exc


class CreatorBasedResource:
    id: int
    created_by_id: int
        

TCreatorBasedResource = TypeVar('TCreatorBasedResource', bound=CreatorBasedResource)


class UserBasedDTO(BaseModel, Generic[TCreatorBasedResource]):
    user_id: int
    obj: 'TCreatorBasedResource'

    class Config:
        arbitrary_types_allowed = True


TUserBasedDTO = TypeVar('TUserBasedDTO', bound=UserBasedDTO)


class CreatorBaseDelete(
    RepoBindedApp,
    Interactor[TUserBasedDTO, Union[OutputDTO, None]],
    Generic[TUserBasedDTO, OutputDTO],
):
    async def __call__(self, data: 'TUserBasedDTO'):
        if data.user_id != data.obj.created_by_id:
            raise exc.ApplicationError(details="Has not access to delete resource!")

        await self.repo.delete(data.obj.id)
