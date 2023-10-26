import tkinter as tk
from tkinter import filedialog
import os

# Create the root window
root = tk.Tk()
root.title('notepad')
root.geometry("400x410")

# Set the default save and open path
default_path = os.path.expanduser("~/Documents")


class TextField:
    def __init__(self, root):
        self.text_field = tk.Text(root)
        self.text_field.pack(fill=tk.BOTH, expand=True)
        self.file_path = None  # Variable to store the file path

    def save_file_without_dialog(self):
        if self.file_path:  # If a file path exists, save the file without the dialog
            text = self.text_field.get("1.0", "end-1c")
            with open(self.file_path, "w") as file:
                file.write(text)

    def get_text(self):
        return self.text_field.get("1.0", "end-1c")


text_field = TextField(root)


def save_file(event=None):
    # Get the text from the text field
    text = text_field.get_text()
    # Check if a file path exists
    if text_field.file_path:
        # Save the file without the dialog
        with open(text_field.file_path, "w") as file:
            file.write(text)
    else:
        # Show the save dialog
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialdir=default_path)
        if file_path:
            with open(file_path, "w") as file:
                file.write(text)
                text_field.file_path = file_path


def save_file_as(event=None):
    if text_field.file_path:  # If a file path exists, save the file without the dialog
        text_field.save_file_without_dialog()
    else:  # If no file path exists, show the save dialog
        text = text_field.get_text()
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialdir=default_path)
        if file_path:
            with open(file_path, "w") as file:
                file.write(text)
            text_field.file_path = file_path


def open_file(event=None):
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    file_path = filedialog.askopenfilename(filetypes=filetypes, initialdir=default_path)
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text_field.text_field.delete('1.0', tk.END)
            text_field.text_field.insert('1.0', content)
        text_field.file_path = file_path


class Menus:
    def __init__(self):
        self.menus()

    def menus(self):
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        apperance = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="Appearance", menu=apperance)
        filemenu.add_command(label='Open', command=open_file)
        filemenu.add_command(label="Save", command=save_file)
        filemenu.add_command(label='Save as', command=save_file_as)
        root.config(menu=menubar)


class Binds:
    def __init__(self):
        root.bind("<Control-s>", save_file)
        root.bind("<Control-o>", open_file)


binds = Binds()
menus = Menus()
root.mainloop()
