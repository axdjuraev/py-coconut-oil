from typing import TYPE_CHECKING, Annotated, Generic, TypeVar
from dishka import FromDishka


TReq = TypeVar('TReq')


class TDepMetaclass(type):
    def __getitem__(cls, key: TReq) -> TReq:
        return FromDishka[key]  # type: ignore


if TYPE_CHECKING:
    IDependency = Annotated[TReq, Generic[TReq]]
else:
    class IDependency(metaclass=TDepMetaclass):
        pass
