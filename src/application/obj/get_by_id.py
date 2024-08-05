from typing import TypeAlias
from src.domain.models import OutObjSchema
from src.application.common import GetByID, IDBindedDTO
from .repo_binded import RepoBindedApp


class GetObjByIDDTO(IDBindedDTO):
    id: int


class GetObjByID(
    RepoBindedApp,
    GetByID[GetObjByIDDTO, OutObjSchema],
):
    DTO: TypeAlias = GetObjByIDDTO 
