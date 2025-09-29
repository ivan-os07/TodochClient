from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext


from states import RegistrationForm

router = Router()


@router.message(Command(commands=["registration"]))
async def registration_start(message: Message, state: FSMContext) -> None:
    await state.set_state(RegistrationForm.username)
    await message.answer(
        "Hi there! What's your username?",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message(RegistrationForm.username)
async def process_name(message: Message, state: FSMContext) -> None:
    data = await state.update_data(name=message.text)
    await state.clear()

    print(data)
    # реализовать проверку midleware на наличие username
