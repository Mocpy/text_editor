#!/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog

#def text():
#    text_area = tk.Text(root)
#    text_area.pack()

root = tk.Tk()
root.title('notepad')
root.geometry("400x410")



text_field = tk.Text(root)
text_field.pack()


def save_file():
    text = text_field.get("1.0", "end-1c")
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
    f = filedialog.askopenfile(filetypes=filetypes)
    # read the text file and show its content on the Text
    text_field.insert('1.0', f.readlines())

class Menues:
    def menues(self):
    
        menubar = tk.Menu(root)
        FileMenu = tk.Menu(menubar, tearoff=0)
        HelpMenu = tk.Menu(menubar, tearoff=0)

        menubar.add_cascade(label="File", menu=FileMenu)

        menubar.add_cascade(label="Nápověda", menu=HelpMenu)

        FileMenu.add_command(label="Save", command=save_file)
        FileMenu.add_command(label='Open', command=open_file)
        

        root.config(menu=menubar)





Menues.menues('self')

root.mainloop()
