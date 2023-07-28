

import tkinter as tk
from pathlib import Path
from tkinter import filedialog
from tkinter.ttk import Progressbar

import PyPDF2
import comtypes.client as cc
from tkinter import messagebox
from fpdf import FPDF

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

global file_path
file_path=""


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
    # Open file dialog to select a Word document
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        messagebox.showinfo("Selected Word document:", file_path)
        canvas.create_text(210.0,
                           220.0,
                           anchor="nw",
                           text="File Name : " + file_path,
                           fill="#000000",
                           font=("Tienne Regular", 12 * -1))


def button2_clicked():
    if file_path:
        global output_file
        output_file =filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt")])
        if not output_file:
            messagebox.showinfo("No Output File", "Please provide an output file name.")
            return

        try:
            with open(file_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                num_pages = len(reader.pages)
                text = ""

                for page_num in range(num_pages):
                    page = reader.pages[page_num]
                    text += page.extract_text()

            with open(output_file+".txt", "w") as file:
                file.write(text)

            messagebox.showinfo("Extraction Successful",
                                f"Text extracted from {num_pages} pages and saved to {output_file} ")
            button_3.config(cursor="hand2" , state="normal")

        except Exception as e:
            messagebox.showerror("Extraction Error", f"An error occurred during text extraction: {str(e)}")
            window.title("PDF TO TXT CONVERTER")
            messagebox.showinfo("" ,"Please provide an output file name.")
            button_3.config(state="normal", cursor="hand2")

    else:
        window.title("PDF TO TXT CONVERTER")
        messagebox.showinfo("" ,"Please select a txt file first.")


def button3_clicked():
       import os
       os.startfile(output_file+".txt")
       window.destroy()



window = tk.Tk()
window.title("PDF TO TXT CONVERTER")
window.geometry("773x458")
window.configure(bg = "#FFFFFF")


canvas = tk.Canvas(
    window,
    bg = "#FFFFFF",
    height = 458,
    width = 773,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = tk.PhotoImage(
    file=r'pdf2txt\image_1.png')
image_1 = canvas.create_image(
    386.0,
    229.0,
    image=image_image_1
)

canvas.create_text(
    215.0,
    57.0,
    anchor="nw",
    text="PDF To TXT Converter",
    fill="#000000",
    font=("Tienne Regular", 28 * -1)
)

button_image_1 = tk.PhotoImage(
    file=r'pdf2txt\button_1.png')
button_1 = tk.Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=button1_clicked,
    relief="flat"
)
button_1.place(
    x=127.0,
    y=158.0,
    width=229.0,
    height=48.0
)

button_image_2 = tk.PhotoImage(
    file=r'pdf2txt\button_2.png')
button_2 = tk.Button(
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
button_1.config(cursor="hand2")
button_2.config(cursor="hand2")
button_image_3 = tk.PhotoImage(
    file=r'pdf2txt\button_3.png')
button_3 = tk.Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=button3_clicked,
    relief="flat"
)
button_3.place(
    x=272.0,
    y=241.0,
    width=229.0,
    height=48.0
)
button_3.config(state="disabled" , cursor="watch")
window.grab_set()
window.attributes('-topmost', True)
window.focus_force()
center_window()
window.resizable(False, False)
window.mainloop()
