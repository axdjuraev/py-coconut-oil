__all__ = [
    "TUOW",
    "TUOWFactory",
]


from axabc.db import AsyncUOW, AsyncUOWFactory
from .repo_collection import RepoCollection


TUOWFactory = AsyncUOWFactory[RepoCollection]
TUOW = AsyncUOW[RepoCollection]
