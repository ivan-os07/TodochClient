from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


from keyboards import help_kb

router = Router()

a = 10

@router.message(Command(commands=["info", "help", "about"]))
async def command_help_handler(message: Message) -> None:
    try:
        await message.answer(f"CMD help", reply_markup=help_kb)
    except TypeError:
        await message.answer("Nice try!")
