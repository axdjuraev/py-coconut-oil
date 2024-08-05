from abc import ABC, abstractmethod
from axsqlalchemy.repository.common import BaseRepository
from src.domain.types import CommonDependency


class RepoBindedApp(ABC):
    def __init__(
        self,
        cd: CommonDependency,
    ) -> None:
        self.cd = cd

    @property
    @abstractmethod
    def repo(self) -> BaseRepository:
        pass
