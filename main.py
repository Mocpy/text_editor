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


root = tk.Tk()
root.title("Uložit jako .txt")
root.geometry("400x410")

save_button = tk.Button(root, text="Uložit", command=save_text)
save_button.pack()

text_area = tk.Text(root)
text_area.pack()


root.mainloop()
