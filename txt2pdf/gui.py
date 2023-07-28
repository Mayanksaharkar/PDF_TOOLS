import tkinter as tk
from pathlib import Path
from tkinter import filedialog
from tkinter import messagebox
from fpdf import FPDF
from reportlab.pdfgen import canvas

OUTPUT_PATH = Path(__file__).parent



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
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        messagebox.showinfo("Selected txt document:", file_path)
        canvas.create_text(210.0, # type: ignore
                           220.0,
                           anchor="nw",
                           text="File Name : " + file_path,
                           fill="#000000",
                           font=("Tienne Regular", 12 * -1))


def button2_clicked():
    if file_path:
        global output_file
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if output_file:
            try:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)

                with open(file_path, "r") as file:
                    for line in file:
                        pdf.cell(0, 10, txt=line, ln=True)

                pdf.output(output_file)
                button_3.config(cursor="hand2", state="normal")
                messagebox.showinfo("Conversion Successful", "Text file converted to PDF successfully!")
            except Exception as e:
                window.title("TXT TO PDF CONVERTER")
                messagebox.showerror("Error", f"An error occurred while converting the document: {e}")


        else:
            window.title("TXT TO PDF CONVERTER")
            messagebox.showinfo("", "Please provide an output file name.")
            button_3.config(state="normal", cursor="hand2")

    else:
        window.title("TXT TO PDF CONVERTER")
        messagebox.showinfo("", "Please select a txt file first.")


def button3_clicked():
    import os
    os.startfile(output_file)
    window.destroy()


window = tk.Tk()
window.title("TXT TO PDF CONVERTER")
window.geometry("773x458")
window.configure(bg="#FFFFFF")

canvas = tk.Canvas(
    window,
    bg="#FFFFFF",
    height=458,
    width=773,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = tk.PhotoImage(
    file=r"txt2pdf\assets\frame0\image_1.png")
image_1 = canvas.create_image(
    386.0,
    229.0,
    image=image_image_1
)

canvas.create_text(
    229.0,
    57.0,
    anchor="nw",
    text="TXT to PDF Converter",
    fill="#000000",
    font=("Tienne Regular", 28 * -1)
)

button_image_1 = tk.PhotoImage(    file=r"txt2pdf\assets\frame0\button_1.png")

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
    file=r"txt2pdf\assets\frame0\button_2.png")
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

button_image_3 = tk.PhotoImage(
    file=r"txt2pdf\assets\frame0\button_3.png")
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
button_3.config(state="disabled", cursor="watch")
button_2.config(cursor="hand2")
button_1.config(cursor="hand2")
window.resizable(False, False)
center_window()
window.mainloop()
