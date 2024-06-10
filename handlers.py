from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Для создания pdf файла с data matrix просто отправьте xlsx документ")


@router.message()
async def file_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id} {msg.from_user.first_name} {msg.text}")