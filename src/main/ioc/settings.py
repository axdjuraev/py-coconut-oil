from dishka import AnyOf, Scope, provide

from src.main.settings import Settings
from src.domain import settings
from .base import BaseIoCProvider


class SettingsIoCProvider(BaseIoCProvider):
    @provide(scope=Scope.APP)
    def _(self) -> AnyOf[
        Settings,
        settings.MinioStoreSettings,
        settings.BaseSettings,
        settings.AppSettings,
        settings.JWTSettings,
    ]:
        return Settings(_env_file='.env')
