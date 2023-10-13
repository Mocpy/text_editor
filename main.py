#!/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('notepad')
root.geometry("400x410")

class TextField:
    def __init__(self, root):
        self.text_field = tk.Text(root)
        self.text_field.pack(fill=tk.BOTH, expand=True)

text_field = TextField(root)

def save_file():
    text = text_field.text_field.get("1.0", "end-1c")
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            file.write(text)

def open_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # show the open file dialog
    file_path = filedialog.askopenfilename(filetypes=filetypes)
    if file_path:
        # read the text file and show its content on the Text
        with open(file_path, "r") as file:
            content = file.read()
            text_field.text_field.delete('1.0', tk.END)  # Clear existing text
            text_field.text_field.insert('1.0', content)

class Menus:
    def menus(self):
        menubar = tk.Menu(root)
        FileMenu = tk.Menu(menubar, tearoff=0)
        HelpMenu = tk.Menu(menubar, tearoff=0)

        menubar.add_cascade(label="File", menu=FileMenu)
        menubar.add_cascade(label="Appearance", menu=HelpMenu)

        FileMenu.add_command(label="Save", command=save_file)
        FileMenu.add_command(label='Open', command=open_file)

        root.config(menu=menubar)

menus = Menus()
menus.menus()

root.mainloop()