import logging
from httpx import AsyncClient


logger = logging.getLogger(__name__)


class ApiAsyncClient(AsyncClient):
    async def request(self, method, url, *args, json=None, **kwargs):
        logger.debug(f"[{method}:{url}]: {json=}; {kwargs.get('headers')=}")
        res = await super().request(method, url, *args, json=json, **kwargs)
        logger.debug(f"[{method}:{url}:{res.status_code}]: {res.read()=}")
        return res
