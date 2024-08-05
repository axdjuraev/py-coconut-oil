from typing import TypeAlias
from src.domain.models import OutObjSchema
from src.application.common import  CreatorBaseDelete, UserBasedDTO
from .repo_binded import RepoBindedApp


class DeleteObjByIDDTO(UserBasedDTO):
    obj: OutObjSchema


class DeleteObjByID(
    RepoBindedApp,
    CreatorBaseDelete[DeleteObjByIDDTO, None],
):
    DTO: TypeAlias = DeleteObjByIDDTO 
