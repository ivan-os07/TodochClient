from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command(commands=["registration"]))
async def registration_handler(message: Message) -> None:
    await message.answer(f"registration process")
