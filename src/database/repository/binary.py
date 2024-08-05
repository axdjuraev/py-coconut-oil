from src.domain.models import BaseBinarySchema as Schema
from src.domain.models import OutBinarySchema as OutSchema
from src.database.models import BinaryModel as Model
from .base import BaseRepository


class BinaryRepository(BaseRepository[Model, Schema, OutSchema]):
    pass
