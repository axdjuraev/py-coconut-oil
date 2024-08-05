from .base import BaseSettings


class MinioStoreSettings(BaseSettings):
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    MINIO_ENDPOINT: str
    MINIO_BUCKET_NAME: str
    MINIO_ENDPOINT_SECURE: bool 
