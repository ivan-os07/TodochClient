from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    if message.from_user:
        await message.answer(f"Hello, <b>{message.from_user.full_name}</b>!")
