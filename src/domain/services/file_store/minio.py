import time
import aiohttp
from miniopy_async import Minio
from typing import IO, Any, Optional, TypeAlias, Union

from pydantic import BaseModel
from .base import FileStoreService


TID: TypeAlias = str


class MinioStoreDTO(BaseModel):
    filename: str
    bf_size: int
    bf: Union[IO, Any]
    content_type: str

    class Config:
        arbitrary_types_allowed=True


class MinioFileStoreService(FileStoreService):
    def __init__(
        self, 
        *, 
        client: Minio, 
        bucket_name: str,
        postfix_format="{time}-{name}",
    ) -> None:
        super().__init__()
        self.client = client
        self.bucket_name = bucket_name
        self.postfix_format = postfix_format
        self.session = aiohttp.ClientSession()

    async def store(self, data: MinioStoreDTO) -> TID:
        destination_path = self.postfix_format.format(
            time=int(time.time()),
            name=data.filename,
        )
        await self.client.put_object(
            self.bucket_name, 
            destination_path, 
            length=data.bf_size,
            data=data.bf,
            content_type=data.content_type,
        )
        return destination_path

    async def load(self, id: TID) -> Optional[bytes]:
        obj = await self.client.get_object(self.bucket_name, id, self.session)

        if (obj) is None:
            return None

        bf = await obj.read()
        obj.release()

        return bf

