import asyncio
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from logger import main_logger

from settings import BotSettings

from handlers import *

settings = BotSettings()


async def main() -> None:
    try:
        bot = Bot(
            token=settings.bot_token,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        )

    except Exception as e:
        main_logger.error(f"Bot initialization failed: {e}")
        sys.exit(1)

    dp = Dispatcher()
    dp.include_routers(start_router, help_router, register_router)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)

    except Exception as e:
        main_logger.exception(f"Error while running the bot: {e}")

    finally:
        # Корректное закрытие сессии
        await bot.session.close()
        main_logger.info("Bot has stopped")


if __name__ == "__main__":
    asyncio.run(main())
