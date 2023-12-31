import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox
import pandas as pd
import tabula


global file_path
file_path = ""



def center_window():
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_width()) // 4
    y = (screen_height - window.winfo_height()) // 4

    # Move the window to the center of the screen
    window.geometry("+{}+{}".format(x, y))


def convertTuple(image_paths):
    str = ''
    for item in image_paths:
        str = str + item
        return str


def button1_clicked():
    # Open file dialog to select an Excel file
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

    if file_path:
        messagebox.showinfo("Selected Excel file:", file_path)

        canvas.create_text(210.0,
                           220.0,
                           anchor="nw",
                           text="File Name : " + file_path,
                           fill="#000000",
                           font=("Tienne Regular", 12 * -1))


def button2_clicked():
    if file_path:
        global output_file
        output_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        if output_file:
            if os.path.exists(output_file):
                result = messagebox.askyesno("Warning", "The output file already exists. Do you want to overwrite it?")
                if result:
                    os.remove(output_file)

                else:
                    return
            window.title("Converting Please Wait!")

            try:
                # Extract table data from the PDF
                tables = tabula.read_pdf(file_path, pages='all')

                # Save each table as a separate sheet in the Excel file
                with pd.ExcelWriter(output_file) as writer:
                    for i, table in enumerate(tables, start=1):
                        table.to_excel(writer, sheet_name=f"Table {i}", index=False)

                messagebox.showinfo("Conversion Successful", "EXCEL file converted to PDF successfully!")
            except Exception as e:
                messagebox.showerror("Conversion Error", f"An error occurred during EXCEL to PDF conversion: {str(e)}")

            window.title("PDF TO EXCEL")
            button_3.config(state="normal")
            button_3.config(cursor="hand2")

            canvas.config(cursor="arrow")
        else:
            messagebox.showinfo("", "Please provide an output file name.")
    else:
        messagebox.showinfo("", "Please select an PDF file first.")


def button3_clicked():
    import os
    os.startfile(output_file)
    window.destroy()


window = Tk()
window.title("PDF TO EXCEL")
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
    file=r'pdf2excel\image_1.png')
image_1 = canvas.create_image(
    386.0,
    229.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=r'pdf2excel\button_1.png')
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

button_image_2 = PhotoImage(
    file=r'pdf2excel\button_2.png')
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

button_image_3 = PhotoImage(
    file=r'pdf2excel\button_3.png')
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

canvas.create_text(
    218.0,
    57.0,
    anchor="nw",
    text="PDF to EXCEL Converter",
    fill="#000000",
    font=("Tienne Regular", 28 * -1)
)

button_3.config(cursor="watch", state="disabled")
button_1.config(cursor="hand2")
button_2.config(cursor="hand2")
window.grab_set()
window.attributes('-topmost', True)
window.focus_force()
center_window()
window.resizable(False, False)
window.mainloop()
