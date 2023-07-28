import os
import tkinter as tk
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Button, PhotoImage
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar

from PIL import Image
from fpdf import FPDF

window = Tk()
window.title("IMAGE TO PDF CONVERTER")
window.geometry("773x458")
window.configure(bg="#FFFFFF")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\mayan\Desktop\py\guis\build\assets\frame4")
global image_paths
image_paths= ""

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def convertTuple(image_paths):
    str = ''
    for item in image_paths:
        str = str + item
        return str


def center_window():
    # Get the screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y coordinates of the center of the screen
    x = (screen_width - window.winfo_width()) // 4
    y = (screen_height - window.winfo_height()) // 4

    # Move the window to the center of the screen
    window.geometry("+{}+{}".format(x, y))


def button1_clicked():
    # Open file dialog to select multiple images
    global image_paths
    image_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if image_paths:
        messagebox.showinfo("Selected images:", image_paths)
        print(type(image_paths))

        canvas.create_text(210.0,
                           220.0,
                           anchor="nw",
                           text="File Name : " + convertTuple(image_paths),
                           fill="#000000",
                           font=("Tienne Regular", 12 * -1))


def button2_clicked():
    if image_paths:
        global output_file
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if output_file:
            if os.path.exists(output_file):
                result = messagebox.askyesno("Warning", "The output file already exists. Do you want to overwrite it?")
                if result:
                    os.remove(output_file)
                else:
                    return
            window.title("Converting Please Wait!")

            # Convert images to PDF
            pdf = FPDF()
            total_pages = len(image_paths)
            for i, image_path in enumerate(image_paths):
                pdf.add_page()
                pdf.image(image_path, 0, 0, pdf.w, pdf.h)

            # Save PDF file
            pdf.output(output_file, "F")
            window.title("IMAGE TO PDF CONVERTER")
            messagebox.showinfo("Success", "Images converted to PDF successfully!")
            button_3.config(state="normal")
            button_3.config(cursor="hand2")

        else:
            messagebox.showinfo("","Please provide an output file name.")

    else:
        messagebox.showinfo("","Please select images first.")


def button3_clicked():
    import os
    os.startfile(output_file)
    window.destroy()






canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=458,
    width=773,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=r'img2pdf\image_1.png')
image_1 = canvas.create_image(
    386.0,
    229.0,
    image=image_image_1
)

canvas.create_text(
    216.0,
    57.0,
    anchor="nw",
    text="Image to PDF Converter",
    fill="#000000",
    font=("Tienne Regular", 28 * -1)
)

button_image_1 = PhotoImage(
    file=r'img2pdf\button_1.png')
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=button1_clicked,
    relief="flat"
)
button_1.config(cursor="hand2")
button_1.place(
    x=127.0,
    y=158.0,
    width=229.0,
    height=48.0
)

button_image_2 = PhotoImage(
    file=r'img2pdf\button_2.png')
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=button2_clicked,
    relief="flat"
)
button_2.place(
    x=417.0,
    y=158.0,
    width=229.0,
    height=48.0
)
button_2.config(cursor="hand2")

button_image_3 = PhotoImage(
    file=r'img2pdf\button_3.png')
button_3 = Button(
    borderwidth=0,
    highlightthickness=0,
    command=button3_clicked,
    relief="flat",
    text="Open",
    image=button_image_3
)
button_3.config(state="disabled")

button_3.place(
    x=272.0,
    y=239.0,
    width=229.0,
    height=50.0
)
button_3.config(cursor="watch")

window.grab_set()
window.attributes('-topmost', True)
window.focus_force()
center_window()
window.resizable(False, False)
window.mainloop()