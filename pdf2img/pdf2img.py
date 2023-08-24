import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog
import os
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
from pdf2image import convert_from_path
import time
from tkinter import messagebox

global file_path
file_path = ""


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
    # Open file dialog to select a PDF file
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        print("Selected Image file:", file_path)

    canvas.create_text(210.0,
                       220.0,
                       anchor="nw",
                       text="File Name : " + file_path,
                       fill="#000000",
                       font=("Tienne Regular", 12 * -1))


def button2_clicked():
    if file_path:
        global output_folder
        output_folder = file_path.replace(".pdf", "-images")
        window.title("CONVERTING,PLEASE WAIT!")
        os.makedirs(output_folder, exist_ok=True)
        images = convert_from_path(file_path)
        num_images = len(images)

        # Create progress bar
        progress_window = tk.Toplevel(window)
        progress_window.title("Conversion Progress")
        progress_bar = Progressbar(progress_window, length=300, maximum=num_images)
        progress_bar.pack(pady=10)

        # Simulate a minimum conversion time of 7 seconds
        start_time = time.time()
        elapsed_time = 0

        for i, image in enumerate(images):
            image.save(f"{output_folder}/page_{i + 1}.png")
            progress_bar['value'] = i + 1
            progress_bar.update()

            # Calculate the elapsed time
            elapsed_time = time.time() - start_time
            if elapsed_time < 7:
                remaining_time = 7 - elapsed_time
                time.sleep(remaining_time / num_images)

        progress_window.destroy()
        messagebox.showinfo("Conversion Complete", "PDF converted and images saved successfully!")
        window.title("PDF TO IMAGE CONVERTER ")
        button_3.config(state="normal", cursor="watch")
    else:
        window.title("PDF TO IMAGE CONVERTER ")
        messagebox.showinfo("", "Please select a PDF file first.")


def button3_clicked():
    import os
    os.startfile(output_folder)
    window.destroy()


window = Tk()
window.title("PDF TO IMAGE CONVERTER ")
window.geometry("773x458")
window.configure(bg="#FFFFFF")

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
    file=r'pdf2img\image_1.png')
image_1 = canvas.create_image(
    386.0,
    229.0,
    image=image_image_1
)

canvas.create_text(
    216.0,
    57.0,
    anchor="nw",
    text="PDF to Image Converter",
    fill="#000000",
    font=("Tienne Regular", 28 * -1)
)

button_image_1 = PhotoImage(
    file=r'pdf2img\button_1.png')
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
    file=r'pdf2img\button_2.png')
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
    file=r'pdf2img\button_3.png')
button_3 = Button(
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
button_3.config(cursor="watch", state="disabled")
window.grab_set()
window.attributes('-topmost', True)
window.focus_force()
center_window()
window.resizable(False, False)
window.mainloop()
