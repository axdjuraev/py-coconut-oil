from typing import TypeAlias
from src.application.common import  CreatorBaseDelete, UserBasedDTO
from src.domain.models.tag import OutTagSchema
from .repo_binded import RepoBindedApp


class DeleteTagByIDDTO(UserBasedDTO):
    obj: OutTagSchema


class DeleteTagByID(
    RepoBindedApp, 
    CreatorBaseDelete[DeleteTagByIDDTO, None]
):
    DTO: TypeAlias = DeleteTagByIDDTO 
