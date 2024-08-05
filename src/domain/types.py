from dataclasses import dataclass
from src.database.types import TUOW


@dataclass
class CommonDependency:
    uow: TUOW 
