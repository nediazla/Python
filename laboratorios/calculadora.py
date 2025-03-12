import tkinter as tk  # Importa la librería tkinter para crear la interfaz gráfica de usuario
from tkinter import messagebox  # Importa el módulo messagebox para mostrar mensajes emergentes
import math  # Importa la librería math, aunque no se utiliza en este código

# Función que se ejecuta cuando un botón es presionado
def on_button_click(value):
    current_text = entry.get()  # Obtiene el texto actual del campo de entrada (pantalla de la calculadora)

    if value == "=":  # Si el valor del botón es "=" (botón de igual)
        try:
            result = eval(current_text)  # Intenta evaluar la expresión matemática que está en el texto de la pantalla
            entry.delete(0, tk.END)  # Borra el contenido de la pantalla
            entry.insert(tk.END, str(result))  # Inserta el resultado de la evaluación en la pantalla
        except Exception as e:  # Si ocurre algún error (como una expresión inválida)
            messagebox.showerror('Error', 'Entrada invalida')  # Muestra un mensaje de error
            entry.delete(0, tk.END)  # Borra el contenido de la pantalla
    elif value == "C":  # Si el valor del botón es "C" (botón de borrar)
        entry.delete(0, tk.END)  # Borra todo el contenido de la pantalla
    else:
        entry.insert(tk.END, value)  # Si el valor del botón es un número o un operador, lo agrega a la pantalla

# Función para crear y configurar la calculadora
def create_calculator():
    root = tk.Tk()  # Crea la ventana principal de la aplicación
    root.title("Calculadora")  # Establece el título de la ventana
    root.geometry("550x600")  # Define las dimensiones de la ventana (550x600 píxeles)

    global entry  # Declara la variable entry a nivel global para poder acceder a ella desde otras funciones
    entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid", justify="right")
    # Crea un campo de entrada para la pantalla de la calculadora con propiedades de diseño
    entry.grid(row=0, column=0, columnspan=4)  # Coloca el campo de entrada en la parte superior (primera fila y 4 columnas)

    # Lista de botones con sus valores y posiciones en la cuadrícula
    buttons = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ("C", 5, 0),
    ]

    # Crea los botones según la lista anterior y los coloca en la cuadrícula
    for (text, row, col) in buttons:
        button = tk.Button(root, text=text, width=10, height=3, font=('Arial', 14),
                           command=lambda value=text: on_button_click(value))
        button.grid(row=row, column=col, padx=5, pady=5)  # Añade cada botón en la posición correspondiente

    root.mainloop()  # Ejecuta el bucle principal de la interfaz gráfica de usuario

# Esta sección se ejecuta si el script es el principal
if __name__ == "__main__":
    create_calculator()  # Llama a la función para crear y mostrar la calculadora
