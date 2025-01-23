# Ejercicio 1: Longitud y ancho de un rectángulo, área y perímetro
# Descripción: Solicita al usuario la longitud y el ancho de un rectángulo, luego calcula su área y perímetro.
longitud = float(input("Ingresa la longitud del rectángulo: "))
ancho = float(input("Ingresa el ancho del rectángulo: "))
area = longitud * ancho
perimetro = 2 * (longitud + ancho)
print(f"Área del rectángulo: {area}")
print(f"Perímetro del rectángulo: {perimetro}")

# Ejercicio 2: Cálculo del área y circunferencia de un círculo
# Descripción: Solicita el radio de un círculo y calcula su área y circunferencia, usando pi = 3.14.
radio = float(input("Ingresa el radio del círculo: "))
pi = 3.14
area_circulo = pi * (radio ** 2)
circunferencia = 2 * pi * radio
print(f"Área del círculo: {area_circulo}")
print(f"Circunferencia del círculo: {circunferencia}")

# Ejercicio 3: Pendiente, intersección con el eje X y Y de la ecuación y = 2x - 2
# Descripción: Calcula la pendiente y las intersecciones con los ejes X y Y de la ecuación y = 2x - 2.
m = 2  # pendiente
b = -2  # intersección con el eje Y
x_interseccion = -b / m  # Intersección con el eje X
print(f"Pendiente: {m}")
print(f"Intersección con el eje X: {x_interseccion}")
print(f"Intersección con el eje Y: {b}")

# Ejercicio 4: Pendiente y distancia euclidiana entre los puntos (2, 2) y (6, 10)
# Descripción: Calcula la pendiente y la distancia euclidiana entre los puntos (2, 2) y (6, 10).
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente = (y2 - y1) / (x2 - x1)
distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print(f"Pendiente: {pendiente}")
print(f"Distancia euclidiana: {distancia}")

# Ejercicio 5: Comparación de pendientes
# Descripción: Compara la pendiente calculada en los ejercicios 3 y 4.
pendiente_rectangulo = 2  # Esto es de y = 2x - 2 (de Ejercicio 3)
print(f"Las pendientes son iguales: {pendiente_rectangulo == pendiente}")

# Ejercicio 6: Calcula el valor de y = x^2 + 6x + 9 y determina el valor de x donde y = 0
# Descripción: Calcula el valor de y para diferentes valores de x en la ecuación y = x^2 + 6x + 9, y encuentra donde y = 0.
def calcular_y(x):
    return x**2 + 6*x + 9

for x in range(-10, 11):
    y = calcular_y(x)
    print(f"Para x = {x}, y = {y}")

x_0 = -3  # Resolviendo la ecuación y = 0, x = -3
print(f"El valor de x cuando y = 0 es x = {x_0}")

# Ejercicio 7: Longitud de las cadenas y comparación falsa
# Descripción: Compara la longitud de las cadenas 'python' y 'dragon', luego realiza una afirmación falsa.
cadena1 = 'python'
cadena2 = 'dragon'
print(f"Longitud de 'python': {len(cadena1)}")
print(f"Longitud de 'dragon': {len(cadena2)}")
print(f"La comparación de longitudes es falsa: {len(cadena1) == len(cadena2)}")

# Ejercicio 8: Uso del operador *and* para comprobar si 'on' está en ambas cadenas
# Descripción: Verifica si la subcadena 'on' está presente tanto en 'python' como en 'dragon'.
print('on' in cadena1 and 'on' in cadena2)

# Ejercicio 9: Comprobar si 'jargon' está en la oración
# Descripción: Verifica si la palabra 'jargon' está presente en la oración dada.
oracion = "Espero que este curso no esté lleno de jerga"
print('jargon' in oracion)

# Ejercicio 10: Comprobación de la ausencia de 'on' en 'python' y 'dragon'
# Descripción: Verifica si la subcadena 'on' no está presente en ninguna de las cadenas 'python' y 'dragon'.
print('on' not in cadena1 and 'on' not in cadena2)

# Ejercicio 11: Longitud de 'python', conversión a float y luego a string
# Descripción: Calcula la longitud de la cadena 'python', la convierte a float y luego a string.
texto = 'python'
longitud = len(texto)
float_val = float(longitud)
string_val = str(float_val)
print(f"Longitud: {longitud}, como float: {float_val}, como string: {string_val}")

# Ejercicio 12: Comprobación si un número es par
# Descripción: Solicita un número y verifica si es par o no.
numero = int(input("Ingresa un número para comprobar si es par: "))
es_par = numero % 2 == 0
print(f"¿Es el número par? {es_par}")

# Ejercicio 13: Comprobar si la división de piso de 7 por 3 es igual a 2
# Descripción: Verifica si la división de piso de 7 entre 3 es igual a la conversión a entero de 2.7.
division_piso = 7 // 3
numero_convertido = int(2.7)
print(division_piso == numero_convertido)

# Ejercicio 14: Comparar el tipo de '10' con el tipo de 10
# Descripción: Compara si el tipo de '10' (string) es igual al tipo de 10 (entero).
print(type('10') == type(10))

# Ejercicio 15: Comparar si int('9.8') es igual a 10
# Descripción: Verifica si el valor entero de '9.8' es igual a 10.
print(int(float('9.8')) == 10)

# Ejercicio 16: Calcular el salario basado en horas y tarifa por hora
# Descripción: Solicita al usuario las horas trabajadas y la tarifa por hora, y luego calcula el salario semanal.
horas = float(input("Ingresa el número de horas trabajadas: "))
tarifa = float(input("Ingresa la tarifa por hora: "))
salario = horas * tarifa
print(f"Tu salario semanal es {salario}")

# Ejercicio 17: Calcular los segundos vividos basado en los años
# Descripción: Solicita al usuario su edad en años y calcula los segundos vividos, asumiendo 365 días por año.
años = int(input("Ingresa la cantidad de años que has vivido: "))
segundos_vividos = años * 365 * 24 * 60 * 60
print(f"Has vivido {segundos_vividos} segundos.")

# Ejercicio 18: Mostrar la tabla de 
# Descripción: Imprime una tabla con los valores en el formato solicitado.

for i in range(1, 6):  # Para cada número de 1 a 5
    # Imprimir la primera columna (es i)
    row = [i]  
    # Las siguientes columnas son los potencias de i (i^1, i^2, i^3, i^4)
    for j in range(1, 5):
        row.append(i ** j)  # Añadir las potencias de i a la fila
    print(*row)  # Imprimir la fila, con los valores separados por espacios
