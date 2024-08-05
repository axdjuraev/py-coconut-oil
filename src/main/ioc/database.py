from typing import AsyncGenerator
from dishka import Scope, provide

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from axabc.db.async_uowf import AsyncUOWFactory
from sqlalchemy.orm import sessionmaker

from src.database.repo_collection import RepoCollection
from src.database.types import TUOW, TUOWFactory
from src.main.settings import Settings
from .base import BaseIoCProvider


class DatabaseIoCProvider(BaseIoCProvider):
    @provide(scope=Scope.APP)
    def get_engine(self, settings: Settings) -> AsyncEngine:
        return create_async_engine(settings.db_connection_string)

    @provide(scope=Scope.APP)
    def get_session_maker(self, engine: AsyncEngine) -> sessionmaker:
        return sessionmaker(
            engine,  # type: ignore
            class_=AsyncSession,  # type: ignore
            expire_on_commit=False,
        )

    @provide(scope=Scope.APP)
    def get_settings(self, sm: sessionmaker) -> TUOWFactory:
        return AsyncUOWFactory(RepoCollection, sm)  # type: ignore

    @provide(scope=Scope.REQUEST)
    async def get_uowf(self, uowf: TUOWFactory) -> AsyncGenerator[TUOW, None]:
        async with uowf() as uow:
            yield uow
