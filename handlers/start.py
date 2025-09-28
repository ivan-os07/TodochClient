from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards import start_kb

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    if message.from_user:
        await message.answer(f"Hello, <b>{message.from_user.full_name}</b>!")
        await message.answer(
            f"Todoch is your <b>simple</b> and <b>effective</b> manager of your thoughts\n<i>To use our product, you need to register</i>",
            reply_markup=start_kb,
        )
