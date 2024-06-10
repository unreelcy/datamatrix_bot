from pylibdmtx.pylibdmtx import encode, decode
from PIL import Image
from openpyxl import load_workbook
from datetime import datetime


def str_to_str_with_gs(txt: str):
    return txt[:31] + '' + txt[31:37] + '' + txt[37:]


def save_pdf_dmtrx(data: list, file_name: str) -> str:
    data_pdf = []
    for indx in range(len(data)):
        txt = str_to_str_with_gs(data[indx][0])
        encoded = encode(txt.encode('utf8'))
        img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
        data_pdf.append(img)
    data_pdf[0].save(f"Converted_files/{file_name}.pdf", save_all=True, append_images=data_pdf[1:])  # сейвит в pdf`ки

    return f"Converted_files/{file_name}.pdf"


def save_png_one_txt(line: str):
    txt = str_to_str_with_gs(line)
    encoded = encode(txt.encode('utf8'))
    img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
    img.save(f'done_files\dmtx_1.png') # сейвит в png`шки


def open_xlsx_to_data(file_path: str):
    book = load_workbook(file_path)
    sheet = book.active
    data = []

    i = 1
    while sheet[f'B{i}'].value:
        if len(sheet[f'B{i}'].value) >= 83:
            data.append([sheet[f'B{i}'].value, sheet[f'C{i}'].value])
            i += 1
    return data


def do_magic(file_path: str) -> str:
    data = open_xlsx_to_data(file_path)
    return save_pdf_dmtrx(data, datetime.now().strftime("%d.%m.%Y-%H.%M.%S"))


if __name__ == '__main__':
    pass
    # data = [i.replace('\n', '') for i in open("test files/data.txt")]
    # save_pdf_dmtrx(data, 'test1')
    # # save_png_dtmrx(data)
    # print(datetime.now().strftime("%d.%m.%Y-%H.%M.%S"))
