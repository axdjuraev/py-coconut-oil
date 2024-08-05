from typing import Generic, TypeVar
from pydantic import BaseModel


TPageData = TypeVar('TPageData')
    

class PageRequireData(BaseModel):
    page: int
    page_size: int


class PageMetadata(PageRequireData):
    total_size: int


class Page(BaseModel, Generic[TPageData]):
    data: list[TPageData]
    meta: PageMetadata
