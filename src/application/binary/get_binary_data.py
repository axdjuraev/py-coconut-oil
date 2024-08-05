from typing import TypeAlias
from src.application.interactor import Interactor
from src.domain.models.binary import OutBinarySchema
from src.domain.services.file_store.minio import MinioFileStoreService
from src.domain.types import CommonDependency
from .repo_binded import RepoBindedApp


class GetBinaryDataDTO(OutBinarySchema):
    pass


class GetBinaryData(
    RepoBindedApp,
    Interactor[GetBinaryDataDTO, bytes],
):
    DTO: TypeAlias = GetBinaryDataDTO 

    def __init__(
        self, 
        cd: CommonDependency,
        minio_fs: MinioFileStoreService,
    ) -> None:
        self.minio_fs = minio_fs
        super().__init__(cd)

    async def __call__(self, data: 'DTO'):
        return await self.minio_fs.load(data.path)
