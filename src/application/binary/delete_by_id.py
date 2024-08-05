from typing import TypeAlias
from src.application.common import  CreatorBaseDelete, UserBasedDTO
from src.domain.models.binary import OutBinarySchema
from .repo_binded import RepoBindedApp


class DeleteBinaryByIDDTO(UserBasedDTO):
    obj: OutBinarySchema


class DeleteBinaryByID(
    RepoBindedApp, 
    CreatorBaseDelete[DeleteBinaryByIDDTO, None]
):
    DTO: TypeAlias = DeleteBinaryByIDDTO 
