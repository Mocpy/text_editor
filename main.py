#!/usr/bin/python3
# -*- coding: utf-8 -*-
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


text_field = TextField(root)


def save_file(event=None):
    # Get the text from the text field
    text = text_field.text_field.get("1.0", "end-1c")
    # Ask the user for a file path to save
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialdir=default_path)
    if file_path:   # If a file path is selected, open the file in write mode and write the text to it
        with open(file_path, "w") as file:
            file.write(text)


def open_file(event=None):
    # Define the file types to be displayed in the open file dialog
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # Show the open file dialog and get the selected file path
    file_path = filedialog.askopenfilename(filetypes=filetypes, initialdir=default_path)
    if file_path:
        # If a file path is selected, read the file and display its content in the text field
        with open(file_path, "r") as file:
            content = file.read()
            text_field.text_field.delete('1.0', tk.END)  # Clear existing text
            text_field.text_field.insert('1.0', content)


class Menus:
    def __init__(self):
        self.menus()

    def menus(self):
        menubar = tk.Menu(root)    # Create the menubar
        # Create the file and Appearance menus
        FileMenu = tk.Menu(menubar, tearoff=0)
        Appearance = tk.Menu(menubar, tearoff=0)

        # Add the file and Appearance menus to the menubar
        menubar.add_cascade(label="File", menu=FileMenu)
        menubar.add_cascade(label="Appearance", menu=Appearance)

        # Add commands to the file menu
        FileMenu.add_command(label="Save", command=save_file)
        FileMenu.add_command(label='Open', command=open_file)

        # Configure the root window to use the menubar
        root.config(menu=menubar)


class Binds:
    def __init__(self):
        root.bind("<Control-s>", save_file)  # Ctrl + S to save file
        root.bind("<Control-o>", open_file)  # Ctrl + O to open file


binds = Binds()    # Create an instance of the Binds class
menus = Menus()    # Create an instance of the Menus class


# Start the main event loop
root.mainloop()
