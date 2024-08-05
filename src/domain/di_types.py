from typing import TypeAlias

from src.database.types import TUOW as _TUOW
from src.domain.types import CommonDependency
from src.utils.di_types import IDependency


TUoW: TypeAlias = IDependency[_TUOW]
TCommonDep: TypeAlias = IDependency[CommonDependency]
