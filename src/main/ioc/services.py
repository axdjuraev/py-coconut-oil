from dishka import AnyOf, Scope, provide
from miniopy_async import Minio

from src.domain.settings.jwt import JWTSettings
from src.domain.settings.minio_store import MinioStoreSettings
from src.domain.types import CommonDependency
from src.domain.services import file_store, auth
from .base import BaseIoCProvider


class ServicesIoCProvider(BaseIoCProvider):
    cd = provide(CommonDependency, scope=Scope.REQUEST)

    @provide(scope=Scope.APP)
    def get_minio_client(self, settings: MinioStoreSettings) -> Minio:
        return Minio(
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            endpoint=settings.MINIO_ENDPOINT,
            secure=settings.MINIO_ENDPOINT_SECURE,
        )

    @provide(scope=Scope.APP)
    def get_minio_fs(self, client: Minio, settings: MinioStoreSettings) -> file_store.MinioFileStoreService:
        return file_store.MinioFileStoreService(
            client=client,
            bucket_name=settings.MINIO_BUCKET_NAME,
        )

    @provide(scope=Scope.APP)
    def get_auth_system(self, settings: JWTSettings) -> AnyOf[
        auth.JWTAuthSystemService,
        auth.AuthSystemService,
    ]:
        return auth.JWTAuthSystemService(settings)
