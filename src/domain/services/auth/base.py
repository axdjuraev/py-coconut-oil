from abc import ABC, abstractmethod
from typing import Any


class AuthSystemService(ABC):
    @abstractmethod
    def create_payload(self, data, exp_delta) -> Any:
        pass

    @abstractmethod
    def get_payload_data(self, payload: dict) -> Any:
        pass

    @abstractmethod
    def varify_password(self, plain_password, hashed_password) -> Any:
        pass

    @abstractmethod
    def get_password_hash(self, password) -> Any:
        pass

    @abstractmethod
    def create_access_token(self, data: str) -> str:
        pass
    
    @abstractmethod
    def create_refresh_token(self, data) -> Any:
        pass

    @abstractmethod
    def get_token_data(self, token) -> Any:
        pass
