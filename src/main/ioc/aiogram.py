from dishka import Scope, provide
from aiogram import Bot, Dispatcher

from src.domain import settings

from .base import BaseIoCProvider


class AiogramIoCProvider(BaseIoCProvider):
    @provide(scope=Scope.APP)
    def get_dispatcher(self) -> Dispatcher:
        dp = Dispatcher()
        return dp 

    def get_bot(self, settings: settings.AiogramSettings) -> Bot:
        dp = Bot(token=settings.BOT_TOKEN)
        return dp 
