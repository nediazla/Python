# helloworld.py

# 1. Comprobamos la versión de Python que estamos usando
import sys

print("Versión de Python:")
print(sys.version)  # Imprime la versión de Python

# 2. Realizamos las operaciones con los operandos 3 y 4

print("\nOperaciones con 3 y 4:")

# Suma
print("Suma (3 + 4):", 3 + 4)

# Resta
print("Resta (3 - 4):", 3 - 4)

# Multiplicación
print("Multiplicación (3 * 4):", 3 * 4)

# Módulo (resto de la división)
print("Módulo (3 % 4):", 3 % 4)

# División
print("División (3 / 4):", 3 / 4)

# Exponencial
print("Exponencial (3 ** 4):", 3 ** 4)

# División de base (cociente entero)
print("División de base (3 // 4):", 3 // 4)

# 3. Mostramos algunas cadenas
print("\nCadenas:")

# Cadenas
print("Tu nombre")
print("Tu apellido")
print("Tu país")
print("Estoy disfrutando de clases de Python")

# 4. Comprobamos los tipos de datos de varios valores

print("\nTipos de datos:")

# Comprobación de tipos
print("Tipo de 10:", type(10))          # <class 'int'>
print("Tipo de 9.8:", type(9.8))        # <class 'float'>
print("Tipo de 3.14:", type(3.14))      # <class 'float'>
print("Tipo de 4 - 4j:", type(4 - 4j))  # <class 'complex'>
print("Tipo de ['Nelson', 'Python', 'Panama']:", type(['Nelson', 'Python', 'Panama']))  # <class 'list'>
print("Tipo de 'Tu nombre':", type("Tu nombre"))  # <class 'str'>
print("Tipo de 'Tu apellido':", type("Tu apellido"))  # <class 'str'>
print("Tipo de 'Tu país':", type("Tu país"))  # <class 'str'>

# 5. Ejemplos de diferentes tipos de datos de Python

print("\nEjemplos de diferentes tipos de datos en Python:")

# Número entero
entero = 10
print("Número entero:", entero)

# Número flotante
flotante = 9.8
print("Número flotante:", flotante)

# Número complejo
complejo = 4 - 4j
print("Número complejo:", complejo)

# Cadena
cadena = "Hola, soy una cadena"
print("Cadena:", cadena)

# Booleano
booleano = True
print("Booleano:", booleano)

# Lista
lista = [1, 2, 3, 4]
print("Lista:", lista)

# Tupla
tupla = (1, 2, 3)
print("Tupla:", tupla)

# Conjunto (set)
conjunto = {1, 2, 3}
print("Conjunto:", conjunto)

# Diccionario
diccionario = {"nombre": "Juan", "edad": 30}
print("Diccionario:", diccionario)

# 6. Cálculo de la distancia euclidiana entre los puntos (2, 3) y (10, 8)

import math

print("\nCálculo de la distancia euclidiana:")

# Coordenadas de los puntos
x1, y1 = 2, 3
x2, y2 = 10, 8

# Fórmula de la distancia euclidiana
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Imprimimos el resultado
print(f"La distancia euclidiana entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es:", distancia)
