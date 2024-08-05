from typing import Generic

from src.application.interactor import Interactor, InputDTO, OutputDTO
from src.domain.services.auth.base import AuthSystemService
from src.domain.types import CommonDependency
from .repo_binded import RepoBindedApp


class BaseAuthApp(
    RepoBindedApp,
    Interactor[InputDTO, OutputDTO],
    Generic[InputDTO, OutputDTO],
):
    def __init__(
        self, 
        cd: CommonDependency,
        auth_system: AuthSystemService,
    ) -> None:
        self.auth_system = auth_system
        super().__init__(cd)
