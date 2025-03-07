import tkinter as tk
from tkinter import messagebox


def generar_factura():
    # Aquí se puede agregar lógica para recolectar información de la interfaz
    cliente = 1  # Ejemplo de cliente
    productos = [
        {'id_producto': 1, 'cantidad': 2, 'precio': 5.00},
        {'id_producto': 2, 'cantidad': 3, 'precio': 3.50}
    ]
    registrar_factura(cliente, productos)
    messagebox.showinfo("Factura", "Factura generada exitosamente!")

def iniciar_interfaz():
    root = tk.Tk()
    root.title("Sistema de Facturación")

    # Crear interfaz gráfica (botones, campos de texto, etc.)
    btn_factura = tk.Button(root, text="Generar Factura", command=generar_factura)
    btn_factura.pack()

    root.mainloop()

if __name__ == "__main__":
    iniciar_interfaz()