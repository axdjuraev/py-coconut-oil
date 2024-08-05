import asyncio
import logging
import uvicorn
from axsqlalchemy.utils.creation import create_models

from fastapi import FastAPI
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from sqlalchemy.ext.asyncio import AsyncEngine
from grateful_logging.configure import GratefulLoggingConfigurator

from src.main.ioc import IoCProvider
from src.main.ioc.fastapi import FastApiIoCProvider
from src.database.models import Base as BaseDatabaseModel
from src.presentation.api.setup import register_routers


GratefulLoggingConfigurator().setup_logging('logger-config.json')
logging.basicConfig(level=logging.INFO)


async def create_app():
    container = make_async_container(IoCProvider(), FastApiIoCProvider())

    async with container() as request_container:
        app = await request_container.get(FastAPI)
        engine = await request_container.get(AsyncEngine)

        register_routers(app)
        setup_dishka(container, app)

        await create_models(engine, BaseDatabaseModel)

    return app


async def main():
    app = await create_app()
    logging.info("Starting web server...")
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
