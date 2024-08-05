from axsqlalchemy.schema import BaseModel as _BaseModel


class BaseSchema(_BaseModel):
    class Config(_BaseModel.Config):
        from_attributes = True
