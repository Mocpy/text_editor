#!/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog

def save_text():
    text = text_area.get("1.0", "end-1c")
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            file.write(text)

class Menues:
    def menues(self):
    
        menubar = tk.Menu(root)
        FileMenu = tk.Menu(menubar, tearoff=0)
        HelpMenu = tk.Menu(menubar, tearoff=0)

        menubar.add_cascade(label="File", menu=FileMenu)

        menubar.add_cascade(label="Nápověda", menu=HelpMenu)

        FileMenu.add_command(label="Save", command=save_text)
        

        root.config(menu=menubar)




root = tk.Tk()
root.title("Uložit jako .txt")
root.geometry("400x410")



text_area = tk.Text(root)
text_area.pack()

Menues.menues('self')

root.mainloop()
