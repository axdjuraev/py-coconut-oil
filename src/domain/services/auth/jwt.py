from datetime import timedelta, timezone, datetime
from jose import jwt
from passlib.context import CryptContext

from src.domain.settings import JWTSettings
from .base import AuthSystemService


class JWTAuthSystemService(AuthSystemService):
    def __init__(self, settings: JWTSettings) -> None:
        self.settings = settings
        self.pwd_context = CryptContext(
            schemes=["bcrypt"], 
            deprecated="auto",
        )

    def create_payload(self, data: str, exp_delta: datetime):
        return {"exp": exp_delta, "sub": data}

    def get_payload_data(self, payload: dict):
        return payload.get("sub")

    def varify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def create_token(self, data: str, minutes: int) -> str:
        return self._create_token(data, minutes)
    
    def create_access_token(self, data: str) -> str:
        return self.create_token(data, self.settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    def create_refresh_token(self, data: str) -> str:
        return self.create_token(data, self.settings.REFRESH_TOKEN_EXPIRE_MINUTES)

    def get_token_data(self, token):
        return self.get_payload_data(
            jwt.decode(
                token, 
                self.settings.JWT_SECRET, 
                algorithms=[self.settings.JWT_ALGORITHM]
            )
        )

    def _create_token(self, data: str, minutes: int, salt: str = ''):
        expires_delta = datetime.now(timezone.utc) + timedelta(minutes=minutes)
        return jwt.encode(
            self.create_payload(data, expires_delta), 
            f"{self.settings.JWT_SECRET}{salt}", 
            self.settings.JWT_ALGORITHM,
        )
