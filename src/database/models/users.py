from typing import TypeAlias
import sqlalchemy as sa

from .base import BaseModel


class Users(BaseModel):
    id = sa.Column(sa.BigInteger, primary_key=True)
    email = sa.Column(sa.String(1046))
    username = sa.Column(sa.String(1046))
    password_hash = sa.Column(sa.String())


UsersModel: TypeAlias = Users
