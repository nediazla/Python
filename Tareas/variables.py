# Día 2: Clases de programación en Python

# 3. Declara una variable de nombre y asígnale un valor
nombre = "Juan"

# 4. Declara una variable de apellido y asígnale un valor
apellido = "Pérez"

# 5. Declara una variable de nombre completo y asígnale un valor
nombre_completo = "Juan Pérez"

# 6. Declara una variable de país y asígnale un valor
pais = "México"

# 7. Declara una variable de ciudad y asígnale un valor
ciudad = "Ciudad de México"

# 8. Declara una variable de edad y asígnale un valor
edad = 25

# 9. Declara una variable de año y asígnale un valor
año = 2025

# 10. Declara una variable is_married y asígnale un valor
is_married = False

# 11. Declara una variable is_true y asígnale un valor
is_true = True

# 12. Declara una variable is_light_on y asígnale un valor
is_light_on = False

# 13. Declara múltiples variables en una línea
x, y, z = 10, 20, 30

# Ejercicios Nivel 2

# 1. Comprueba el tipo de datos de todas tus variables usando type()
print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(x))
print(type(y))
print(type(z))

# 2. Usando la función incorporada len(), encuentra la longitud de tu nombre
longitud_nombre = len(nombre)
print("Longitud de mi nombre:", longitud_nombre)

# 3. Compara la longitud de tu nombre y tu apellido
longitud_apellido = len(apellido)
print("¿Mi nombre es más largo que mi apellido?", longitud_nombre > longitud_apellido)

# 4. Declara 5 como num_one y 4 como num_two
num_one = 5
num_two = 4

# 5. Suma num_one y num_two y asigna el valor a una variable total
total = num_one + num_two
print("Suma:", total)

# 6. Resta num_two de num_one y asigna el valor a una variable diff
diff = num_one - num_two
print("Resta:", diff)

# 7. Multiplica num_two y num_one y asigna el valor a una variable product
product = num_one * num_two
print("Multiplicación:", product)

# 8. Divide num_one por num_two y asigna el valor a una variable division
division = num_one / num_two
print("División:", division)

# 9. Usa la división de módulo para encontrar num_two dividido por num_one y asigna el valor a una variable remainder
remainder = num_two % num_one
print("Resto de la división:", remainder)

# 10. Calcula num_one a la potencia de num_two y asigna el valor a una variable exp
exp = num_one ** num_two
print("Potencia:", exp)

# 11. Encuentra la división de piso de num_one por num_two y asigna el valor a una variable floor_division
floor_division = num_one // num_two
print("División de piso:", floor_division)

# 12. El radio de un círculo es de 30 metros.
radio = 30

# 13. Calcula el área de un círculo y asigna el valor a una variable llamada area_of_circle
import math
area_of_circle = math.pi * radio ** 2
print("Área del círculo:", area_of_circle)

# 14. Calcula la circunferencia de un círculo y asigna el valor a una variable llamada circum_of_circle
circum_of_circle = 2 * math.pi * radio
print("Circunferencia del círculo:", circum_of_circle)

# 15. Toma el radio como entrada del usuario y calcula el área
radio_usuario = float(input("Introduce el radio del círculo: "))
area_usuario = math.pi * radio_usuario ** 2
print("Área del círculo con el radio proporcionado:", area_usuario)

# 16. Usa la función de entrada incorporada para obtener el nombre, apellido, país y edad de un usuario
nombre_usuario = input("Introduce tu nombre: ")
apellido_usuario = input("Introduce tu apellido: ")
pais_usuario = input("Introduce tu país: ")
edad_usuario = int(input("Introduce tu edad: "))

# Mostrar los datos ingresados
print(f"Nombre: {nombre_usuario}, Apellido: {apellido_usuario}, País: {pais_usuario}, Edad: {edad_usuario}")

# 17. Ejecuta help('keywords') para verificar las palabras clave de Python
help('keywords')
