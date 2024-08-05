from dishka import Scope, provide
from fastapi import FastAPI

from src.domain.settings.app import AppSettings

from .base import BaseIoCProvider


class FastApiIoCProvider(BaseIoCProvider):
    @provide(scope=Scope.APP)
    def get_fastapi_app(self, settings: AppSettings) -> FastAPI:
        app = FastAPI(title=settings.APP_NAME)
        return app
