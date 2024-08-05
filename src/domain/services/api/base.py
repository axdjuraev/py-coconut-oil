from abc import ABC
from httpx import AsyncClient

from src.domain.services.api.api_logger import ApiAsyncClient
from src.domain.settings import BaseSettings


class AsyncApi(ABC):
    def __init__(
        self,
        base_url,
        headers: "dict | None" = None,
        settings: "BaseSettings | None" = None,
        *,
        client: "AsyncClient | None" = None,
    ) -> None:
        self.client = client or ApiAsyncClient(
            base_url=base_url,
            headers=headers,
        )
        self.settings = settings
