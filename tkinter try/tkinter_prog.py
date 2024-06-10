import tkinter as tk
from tkinter import filedialog
from pylibdmtx.pylibdmtx import encode
from PIL import Image
from openpyxl import load_workbook


def str_to_str_with_gs(txt: str):
    return txt[:31] + '' + txt[31:37] + '' + txt[37:]


def save_pdf_dmtrx(data: list, file_name: str):
    data_pdf = []
    for indx in range(len(data)):
        txt = str_to_str_with_gs(data[indx][0])
        encoded = encode(txt.encode('utf8'))
        img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
        data_pdf.append(img)
    data_pdf[0].save(f"{file_name}.pdf", save_all=True, append_images=data_pdf[1:])  # сейвит в pdf`ки


def open_xlsx_to_data(file_path: str):
    book = load_workbook(file_path)
    sheet = book.active
    data = []

    i = 2
    while sheet[f'B{i}'].value:
        data.append([sheet[f'B{i}'].value, sheet[f'C{i}'].value])
        i += 1
    return data


def UploadAction(event=None):
    file_path = filedialog.askopenfilename()
    if file_path.endswith('.xlsx'):
        data = open_xlsx_to_data(file_path)
        save_pdf_dmtrx(data, file_path.split('\\')[-1][:-5])


root = tk.Tk()
button = tk.Button(root, text='upload xlsx file', command=UploadAction)
button.pack()

root.mainloop()