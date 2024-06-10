from aiogram import types, F, Router, MagicFilter, Bot
from aiogram.types import Message
from aiogram.filters import Command
from config import file_directory
from utils import do_magic


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Для создания pdf файла с data matrix просто отправьте xlsx документ")


@router.message(content_types=["document"])
async def file_handler(msg: Message):
    await msg.answer(f"Файл загружается {msg.document.file_name} {msg.document.file_id}")
    await Bot.download_file(msg.document.file_id, destination=format('Downloaded_files' + r'\') + )


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Для работы отправьте файл")
