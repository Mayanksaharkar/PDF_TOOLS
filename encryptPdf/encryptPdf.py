import os


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, simpledialog
import os
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
import time
from tkinter import messagebox
from pypdf import PdfReader, PdfWriter

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

def convertTuple(image_paths):
    str = ''
    for item in image_paths:
        str = str + item
        return str

def show_dialog():
    # Prompt the user for input using a dialog box
    global user_input
    user_input = simpledialog.askstring("PDF Encrypter", "Set Password:")

    if user_input:
        # Display the user's input using a message box
        messagebox.showinfo("User Input", f"Password is : {user_input}")
    else:
        # Display a message if the user cancels the dialog
        messagebox.showinfo("User Input", "No input provided")

def button1_clicked():
    # Open file dialog to select a PDF file
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        print("Selected PDF file:", file_path)

    canvas.create_text(210.0,
                       220.0,
                       anchor="nw",
                       text="File Name : " + file_path,
                       fill="#000000",
                       font=("Tienne Regular", 12 * -1))

def button2_clicked():
    if file_path:
        global output_file
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])

        window.attributes('-topmost', False)
        show_dialog()
        window.title("Encrypting , Please Wait ! ")
        reader = PdfReader(file_path)
        writer = PdfWriter()

        # Add all pages to the writer
        for page in reader.pages:
            writer.add_page(page)

        # Add a password to the new PDF
        writer.encrypt(user_input, algorithm="AES-256")
        
        # Save the new PDF to a file
        with open(output_file, "wb") as f:
            writer.write(f)
        messagebox.showinfo("","PDF Encrypted Successfully")
        window.title("PDF ENCRYPTER")
        button_3.config(state="normal" , cursor="hand2")
    else:
        messagebox.showinfo("","Please select a PDF file first.")


def button3_clicked():
   import os
   os.startfile(output_file)
   window.destroy()

window = Tk()
window.title("PDF ENCRYPTER")
window.geometry("773x458")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 458,
    width = 773,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=r'encryptPdf\image_1.png')
image_1 = canvas.create_image(
    386.0,
    229.0,
    image=image_image_1
)

canvas.create_text(
    276.0,
    57.0,
    anchor="nw",
    text="PDF ENCRYPTER",
    fill="#000000",
    font=("Tienne Regular", 28 * -1)
)

button_image_1 = PhotoImage(
    file=r'encryptPdf\button_1.png')
button_1 = Button(
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
button_1.config(cursor="hand2")

button_image_2 = PhotoImage(
    file=r'encryptPdf\ENCRYPT.png')
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
    file=r'encryptPdf\button_3.png')
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=button3_clicked,
    relief="flat"
)
button_3.config(state="disabled" , cursor="watch")
button_3.place(
    x=272.0,
    y=241.0,
    width=229.0,
    height=48.0
)
window.grab_set()
window.attributes('-topmost', True)
window.focus_force()
center_window()
window.resizable(False, False)
window.mainloop()