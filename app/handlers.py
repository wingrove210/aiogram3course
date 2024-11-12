from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from app.middleware import TestMiddleware
import app.keyboards as kb

router = Router()
router.message.middleware(TestMiddleware())
class Reg(StatesGroup):
    name = State()
    number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Hello {message.from_user.username}, \n {message.from_user.first_name}", reply_markup=kb.main)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('This is command /help')

@router.message(F.text == 'How are you')
async def how_are_you(message: Message):
    await message.answer("I'm good And you")

@router.message(F.photo)
async def photo(message: Message):
    await message.answer(f"Photo ID: {message.photo[-1].file_id}")

@router.message(Command('get_photo'))
async def photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAMLZy6mf4dc8HYKmO9bAqX02n-JXsIAApHjMRu893lJZQiI6Z-yV90BAAMCAAN5AAM2BA', caption='Its a code')

@router.callback_query(F.data=="catalog")
async def catalog(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text("Hey you", reply_markup=await kb.inline_cars())

@router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Enter your name:')


@router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Enter your phone number:')

@router.message(Reg.number)
async def reg_three(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f'thanx for registration ')
    await state.clear()
    
