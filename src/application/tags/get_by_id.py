from typing import TypeAlias
from src.domain.models import OutTagSchema
from src.application.common import GetByID, IDBindedDTO
from .repo_binded import RepoBindedApp


class GetTagByIDDTO(IDBindedDTO):
    pass


class GetTagByID(
    RepoBindedApp,
    GetByID[GetTagByIDDTO, OutTagSchema],
):
    DTO: TypeAlias = GetTagByIDDTO 
