import asyncio
import logging
from axsqlalchemy.utils.creation import create_models
from dataclasses import dataclass

from aiogram import Bot, Dispatcher
from dishka import make_async_container
from dishka.integrations import aiogram as integrations
from sqlalchemy.ext.asyncio import AsyncEngine
from grateful_logging.configure import GratefulLoggingConfigurator

from src.main.ioc import IoCProvider
from src.main.ioc.aiogram import AiogramIoCProvider
from src.database.models import Base as BaseDatabaseModel
from src.presentation.bot.v1 import setup


GratefulLoggingConfigurator().setup_logging('logger-config.json')
logging.basicConfig(level=logging.INFO)


@dataclass
class AiogramApp:
    bot: Bot
    dp: Dispatcher
    db_engine: AsyncEngine


async def create_app():
    container = make_async_container(IoCProvider(), AiogramIoCProvider())

    async with container() as request_container:
        bot = await request_container.get(Bot)
        dp = await request_container.get(Dispatcher)
        engine = await request_container.get(AsyncEngine)

        setup.register_handlers(dp)
        integrations.setup_dishka(container, dp)

        await create_models(engine, BaseDatabaseModel)

    return AiogramApp(bot, dp, engine)


async def main():
    app = await create_app()
    logging.info("Starting aiogram bot polling...")
    app.dp.start_polling(app.bot)



if __name__ == "__main__":
    asyncio.run(main())

