import io

from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from config import file_directory_download
from utils import do_magic
from datetime import datetime


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Для создания pdf файла с data matrix просто отправьте xlsx документ")


@router.message(F.document)
async def file_handler(msg: Message):
    file_name = msg.date.strftime('%d.%m.%Y-%H.%M.%S') + msg.document.file_name
    path = file_directory_download + file_name

    # await msg.answer(f"Файл загружается {file_name}")
    await msg.bot.download(file=msg.document.file_id, destination=path)
    converted_path = do_magic(path, msg.document.file_name)
    doc = FSInputFile(converted_path)
    await msg.reply_document(doc)


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Для обработки отправьте файл xlsx")
