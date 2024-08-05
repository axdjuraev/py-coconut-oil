from axsqlalchemy.model import BaseTable, Base


class BaseModel(BaseTable, Base):
    __abstract__ = True
