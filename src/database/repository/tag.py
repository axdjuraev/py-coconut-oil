from src.domain.models import TagSchema as Schema
from src.domain.models import OutTagSchema as OutSchema
from src.database.models import TagModel as Model
from .base import BaseRepository


class TagRepository(BaseRepository[Model, Schema, OutSchema]):
    pass
