from typing import TypeAlias

from pydantic import BaseModel

from src.application.common import DirectPassCreate
from src.domain.models.binary import BaseBinarySchema, BinarySchema
from src.domain.services.file_store.minio import MinioFileStoreService, MinioStoreDTO
from src.domain.types import CommonDependency
from .repo_binded import RepoBindedApp


class CreateBinaryDTO(BaseModel):
    user_id: int
    meta: MinioStoreDTO


class CreateBinary(
    RepoBindedApp,
    DirectPassCreate[CreateBinaryDTO, None],
):
    DTO: TypeAlias = CreateBinaryDTO 

    def __init__(
        self, 
        cd: CommonDependency,
        minio_fs: MinioFileStoreService,
    ) -> None:
        self.minio_fs = minio_fs
        super().__init__(cd)

    async def prepare_for_store(self, data: 'CreateBinaryDTO'):
        self.repo
        path = await self.minio_fs.store(data.meta)
        return BinarySchema(
            path=path,
            content_type=data.meta.content_type,
            created_by_id=data.user_id,
        )
