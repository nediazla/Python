import tkinter as tk

ventana = tk.Tk()
ventana.title("esta es una ventana")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="bienvenbido a mi ventana")
etiqueta.pack()

boton = tk.Button(ventana, text="hazme click")
boton.pack(side="left", padx=10, pady=10)

camp_texto = tk.Entry(ventana)
camp_texto.pack(side="left", padx=10, pady=10)