from abc import ABC, abstractmethod
from typing import TypeAlias, Any


TID: TypeAlias = Any
TIN_DATA: TypeAlias = Any
TOUT_DATA: TypeAlias = Any


class FileStoreService(ABC):
    @abstractmethod
    async def store(self, data: TIN_DATA) -> TID:
        pass

    @abstractmethod
    async def load(self, id: TID) -> TOUT_DATA:
        pass
