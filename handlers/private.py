from aiogram import types, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import ReplyKeyboardRemove
from filters.type_of_chat import ChatTypeFilter
from keyboards.for_navigate import keyboard
from aiogram.utils.formatting import as_marked_section, Bold, TextLink

private_router = Router()
private_router.message.filter((ChatTypeFilter(["private"])))


@private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Hello", reply_markup=keyboard)


@private_router.message(or_f(Command("options"), F.text.lower() == "options"))
async def option_cmd(message: types.Message):
    await message.answer("options list", reply_markup=keyboard.as_markup(
            resize_keyboard=True,
            input_field_placeholder="Choose your command"
    ))


@private_router.message(Command("about"))
async def option_cmd(message: types.Message):
    await message.answer("info about <b><u>bot</u></b>")


@private_router.message(or_f(Command("links"), F.text.lower() == "links"))
async def option_cmd(message: types.Message):
    text = as_marked_section(
        Bold("Active links"),
        TextLink("study bot", url="https://t.me/task_manager_kiryushe_bot"),
        TextLink("group bot", url="https://t.me/+-P_ukdQI6Pg1YjU6"),
        marker="💥"
    )
    await message.answer(text.as_html())


@private_router.message(Command("homeworks"))
async def option_cmd(message: types.Message):
    await message.answer("all homeworks")


@private_router.message((F.text.lower() == "розклад") | (F.text.contains("schedule")))
@private_router.message(Command("schedule"))
async def option_cmd(message: types.Message):
    await message.answer("our current schedule")
