#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import Tk, Text, Menu, filedialog, PhotoImage
import os


class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Notepad')
        self.root.geometry("400x410")

        icon_path = PhotoImage(file='notepad.434x512.png')
        self.root.iconphoto(False, icon_path)

        self.default_path = os.path.expanduser("~/Documents")
        self.text_field = Text(root)
        self.text_field.pack(fill='both', expand=True)
        self.file_path = None  # Variable to store the file path

        self.setup_menus()
        self.setup_key_bindings()

    def setup_menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label='Open', command=self.open_file)
        file_menu.add_command(label='Save', command=self.save_file)
        file_menu.add_command(label='Save as', command=self.save_file_as)

    def setup_key_bindings(self):
        self.root.bind("<Control-s>", self.save_file)
        self.root.bind("<Control-Shift-S>", self.save_file_as)
        self.root.bind("<Control-o>", self.open_file)

    def save_file(self, event=None):
        text = self.text_field.get("1.0", "end-1c")
        if self.file_path:
            with open(self.file_path, "w") as file:
                file.write(text)
        else:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialdir=self.default_path)
            if file_path:
                with open(file_path, "w") as file:
                    file.write(text)
                    self.file_path = file_path

    def save_file_as(self, event=None):
        text = self.text_field.get("1.0", "end-1c")
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialdir=self.default_path)
        if file_path:
            with open(file_path, "w") as file:
                file.write(text)
            self.file_path = file_path

    def open_file(self, event=None):
        filetypes = (('text files', '*.txt'), ('All files', '*.*'))
        file_path = filedialog.askopenfilename(filetypes=filetypes, initialdir=self.default_path)
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_field.delete('1.0', 'end')
                self.text_field.insert('1.0', content)
            self.file_path = file_path


if __name__ == "__main__":
    root = Tk()
    app = NotepadApp(root)
    root.mainloop()
