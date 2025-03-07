import tkinter as tk
from tkinter import messagebox
import math

from flask.cli import with_appcontext


def create_calculator():
    root = tk.Tk()
    root.title("Calculadora")
    root.geometry('500x600')


    global entry
    entry = tk.Entry(root, width=16, font=('Arial', 20), justify='right', borderwidth=4)
    entry.grid(row=0, column=0, columnspan=4)

    buttons = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("+/-", 4, 0), ("0", 4, 1), (",", 4, 2), ("+", 4, 3)
    ]

    for (text, row, col) in buttons:
        button = tk.Button(root, text=text, width=5, height=3, font=('Arial', 12))
        button.grid(row=row, column=col, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_calculator()
