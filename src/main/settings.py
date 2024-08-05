from src.domain import settings as us


COMMON_SETTINGS = [
    us.MinioStoreSettings,
    us.DatabaseSettings,
    us.AppSettings,
    us.JWTSettings,
]


class Settings(*COMMON_SETTINGS):
    pass
