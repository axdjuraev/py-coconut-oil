from abc import ABC, abstractmethod
from aiogram import Router


class HandlerCollection(ABC):
    @abstractmethod
    def register(self, router: Router) -> Router:
        pass
