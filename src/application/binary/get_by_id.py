from typing import TypeAlias
from src.application.common import GetByID, IDBindedDTO
from src.domain.models.binary import OutBinarySchema
from .repo_binded import RepoBindedApp


class GetBinaryByIDDTO(IDBindedDTO):
    pass


class GetBinaryByID(
    RepoBindedApp,
    GetByID[GetBinaryByIDDTO, OutBinarySchema],
):
    DTO: TypeAlias = GetBinaryByIDDTO 
