import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


def center_window():
    # Get the screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y coordinates of the center of the screen
    x = (screen_width - window.winfo_width()) // 4
    y = (screen_height - window.winfo_height()) // 4

    # Move the window to the center of the screen
    window.geometry("+{}+{}".format(x, y))


def open_compPdf_window():
    subprocess.run(['python', r'compPdf\compPdf.py'])


def open_decryptPdf_window():
    subprocess.run(['python', r'decryptPdf\decryptPdf.py'])


def open_encryptPdf_window():
    subprocess.run(['python', r'encryptPdf\encryptPdf.py'])


def open_excel2pdf_window():
    subprocess.run(['python', r'excel2pdf\excel2pdf.py'])


def open_img2pdf_window():
    subprocess.run(['python', r'img2pdf\img2pdf.py'])


def open_mergePdf_window():
    subprocess.run(['python', r'mergePdf\mergePdf.py'])


def open_pdf2excel_window():
    subprocess.run(['python', r'pdf2excel\pdf2excel.py'])


def open_pdf2img_window():
    subprocess.run(['python', r'pdf2img\pdf2img.py'])


def open_pdf2txt_window():
    subprocess.run(['python', r'pdf2txt\pdf2txt.py'])


def open_pdf2word_window():
    subprocess.run(['python', r'pdf2word\pdf2word.py'])


def open_word2pdf_window():
    subprocess.run(['python', r'word2pdf\word2pdf.py'])


def open_txt2pdf_window():
    subprocess.run(['python', r'txt2pdf\gui.py'])


window = Tk()
window.title("Pdf Tools")

window.geometry("915x505")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=505,
    width=915,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=r"main\build\assets\frame0\image_1.png")
image_1 = canvas.create_image(
    457.0,
    252.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=r"main\build\assets\frame0\button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_pdf2word_window,
    relief="flat"
)
button_1.place(
    x=368.0,
    y=147.0,
    width=180.0,
    height=48.0

)

button_image_2 = PhotoImage(
    file=r"main\build\assets\frame0\button_2.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_compPdf_window,
    relief="flat"
)
button_2.place(
    x=99.0,
    y=340.0,
    width=180.0,
    height=48.0
)

button_image_3 = PhotoImage(
    file=r"main\build\assets\frame0\button_3.png")
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_word2pdf_window,
    relief="flat"
)
button_3.place(
    x=368.0,
    y=212.0,
    width=180.0,
    height=48.0
)

button_image_4 = PhotoImage(
    file=r"main\build\assets\frame0\button_4.png")
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=open_mergePdf_window,
    relief="flat"
)
button_4.place(
    x=367.0,
    y=340.0,
    width=179.99998474121094,
    height=50.0
)

button_image_5 = PhotoImage(
    file=r"main\build\assets\frame0\button_5.png")
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=open_pdf2excel_window,
    relief="flat"
)
button_5.place(
    x=637.0,
    y=145.0,
    width=180.8477783203125,
    height=49.0
)

button_image_6 = PhotoImage(
    file=r"main\build\assets\frame0\button_6.png")
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=open_excel2pdf_window,
    relief="flat"
)
button_6.place(
    x=637.0,
    y=211.0,
    width=180.8477783203125,
    height=49.0
)

button_image_7 = PhotoImage(
    file=r"main\build\assets\frame0\button_7.png")
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=open_encryptPdf_window,
    relief="flat"
)
button_7.place(
    x=636.0,
    y=340.0,
    width=180.0,
    height=48.0
)

button_image_8 = PhotoImage(
    file=r"main\build\assets\frame0\button_8.png")
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=open_decryptPdf_window,
    relief="flat"
)
button_8.place(
    x=636.0,
    y=276.0,
    width=180.0,
    height=48.0
)

button_image_9 = PhotoImage(
    file=r"main\build\assets\frame0\button_9.png")
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=open_txt2pdf_window,
    relief="flat"
)
button_9.place(
    x=99.0,
    y=212.0,
    width=180.0,
    height=48.0
)

button_image_10 = PhotoImage(
    file=r"main\build\assets\frame0\button_10.png")
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=open_pdf2txt_window,
    relief="flat"
)
button_10.place(
    x=99.0,
    y=147.0,
    width=180.0,
    height=48.0
)

button_image_11 = PhotoImage(
    file=r"main\build\assets\frame0\button_11.png")
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=open_pdf2img_window,
    relief="flat"
)
button_11.place(
    x=99.0,
    y=277.0,
    width=180.0,
    height=48.0
)

button_image_12 = PhotoImage(
    file=r"main\build\assets\frame0\button_12.png")
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=open_img2pdf_window,
    relief="flat"
)
button_12.place(
    x=368.0,
    y=277.0,
    width=180.0,
    height=48.0
)

canvas.create_text(
    364.0,
    85.0,
    anchor="nw",
    text="PDF TOOLS",
    fill="#000000",
    font=("Tienne Regular", 32 * -1)
)
center_window()
window.resizable(False, False)
window.mainloop()
