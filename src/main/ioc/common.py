from .application import ApplicationIoCProvider
from .services import ServicesIoCProvider
from .database import DatabaseIoCProvider
from .settings import SettingsIoCProvider


class CommonIoCProvider(
    SettingsIoCProvider,
    ApplicationIoCProvider,
    ServicesIoCProvider,
    DatabaseIoCProvider,
):
    pass
