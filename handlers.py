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


@router.message(F.text.lower().contains('мяу'))
async def start_handler(msg: Message):
    await msg.answer("гав")


@router.message(F.document)
async def file_handler(msg: Message):
    file_name = msg.date.strftime('%d.%m.%Y_%H.%M.%S') + '_' + ''.join(msg.document.file_name.split('.')[:-1])
    await msg.answer(f'Файл {msg.document.file_name} принят.\n Ожидайте обратботки)')

    path = file_directory_download + msg.document.file_name
    await msg.bot.download(file=msg.document.file_id, destination=path)

    converted_path = do_magic(path, file_name)
    doc = FSInputFile(converted_path)
    await msg.answer_document(doc)




@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Для обработки отправьте файл xlsx")
