from pylibdmtx.pylibdmtx import encode, decode
from PIL import Image
from openpyxl import load_workbook
from config import file_directory_convert, file_directory_marks
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import FreeText



def str_to_str_with_gs(txt: str):
    return txt[:31] + '' + txt[31:37] + '' + txt[37:]


def save_pdf_dmtrx(data: list, file_save_path: str):
    data_pdf = []
    for indx in range(len(data)):
        txt = str_to_str_with_gs(data[indx][0])
        encoded = encode(txt.encode('utf8'))
        img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)

        data_pdf.append(img)
    data_pdf[0].save(file_save_path, save_all=True, append_images=data_pdf[1:])  # сейвит в pdf`ки


def add_mark_to_pdf(data: list, file_name: str) -> None:
    reader = PdfReader(file_directory_convert + file_name + '.pdf')
    writer = PdfWriter()
    for i in range(reader.get_num_pages()):
        page = reader.pages[i]
        writer.add_blank_page(200, 210)
        blank_page = writer.pages[i]
        blank_page.merge_page(page, )

        annotation = FreeText(
            text=data[i][1],
            rect=(0, 190, 200, 210),
            font_size="6pt",
            background_color=None,
            border_color=None
        )
        writer.add_annotation(page_number=i, annotation=annotation)

    # Write the annotated file to disk
    with open(file_directory_marks + file_name + '.pdf', "wb") as fp:
        writer.write(fp)


def save_png_one_txt(line: str):
    txt = str_to_str_with_gs(line)
    encoded = encode(txt.encode('utf8'))
    img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
    img.save(f'done_files\dmtx_1.png') # сейвит в png`шки


def open_xlsx_to_data(file_path: str):
    book = load_workbook(file_path)
    sheet = book.active
    data = []

    i = 2
    while sheet[f'B{i}'].value:
        if len(sheet[f'B{i}'].value):
            data.append([sheet[f'B{i}'].value, sheet[f'C{i}'].value])
            i += 1
    return data


def do_magic(file_path: str, file_name: str) -> str:
    print(f'файл {file_path} принят')
    data = open_xlsx_to_data(file_path)
    save_pdf_dmtrx(data, file_directory_convert + file_name + '.pdf')
    add_mark_to_pdf(data, file_name)
    return file_directory_marks + file_name + '.pdf'
