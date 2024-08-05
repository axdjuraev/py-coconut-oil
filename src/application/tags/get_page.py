from typing import TypeAlias
from src.domain.models import OutTagSchema
from src.application.common import GetPage
from .repo_binded import RepoBindedApp
from src.utils import schemas


class GetObjPageDTO(schemas.PageRequireData):
    pass


class GetTagPage(
    RepoBindedApp,
    GetPage[GetObjPageDTO, OutTagSchema],
):
    DTO: TypeAlias = GetObjPageDTO 
