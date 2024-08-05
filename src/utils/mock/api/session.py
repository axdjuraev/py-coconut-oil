import logging
from unittest.mock import AsyncMock


class AsyncSessionMock(AsyncMock):
    async def get(self, *args, **kwargs):
        logging.info(f"[AsyncSessionMock][get]: {args=}; {kwargs=}")
        return await super().get(*args, **kwargs)

    async def post(self, *args, **kwargs):
        logging.info(f"[AsyncSessionMock][post]: {args=}; {kwargs=}")
        return await super().get(*args, **kwargs)

    async def put(self, *args, **kwargs):
        logging.info(f"[AsyncSessionMock][put]: {args=}; {kwargs=}")
        return await super().get(*args, **kwargs)

    async def delete(self, *args, **kwargs):
        logging.info(f"[AsyncSessionMock][delete]: {args=}; {kwargs=}")
        return await super().get(*args, **kwargs)



async def _test():
    session = AsyncSessionMock()
    print(await session.get('test'))


if __name__ == "__main__":
    import asyncio
    asyncio.run(_test())
