from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command(commands=["info", "help", "about"]))
async def command_help_handler(message: Message) -> None:
    try:
        await message.answer(f"CMD help")
    except TypeError:
        await message.answer("Nice try!")
