# Ejercicio 1: Declarar edad como una variable entera
edad = 25  # Declaración de variable entera
print("Mi edad es:", edad)

# Ejercicio 2: Declarar altura como una variable de punto flotante
altura = 1.75  # Declaración de variable flotante
print("Mi altura es:", altura, "metros")

# Ejercicio 3: Declarar una variable que almacene un número complejo
numero_complejo = 3 + 4j  # Número complejo
print("Mi número complejo es:", numero_complejo)

# Ejercicio 4: Calcular el área de un triángulo
# Solicitar al usuario la base y altura del triángulo
base = float(input("Enter base: "))
altura = float(input("Enter height: "))
area_triangulo = 0.5 * base * altura  # Fórmula para calcular el área
print("The area of the triangle is", area_triangulo)

# Ejercicio 5: Calcular el perímetro de un triángulo
# Solicitar al usuario los tres lados del triángulo
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimetro_triangulo = a + b + c  # Fórmula para calcular el perímetro
print("The perimeter of the triangle is", perimetro_triangulo)

# Ejercicio 6: Calcular el área y perímetro de un rectángulo
longitud = float(input("Enter length of the rectangle: "))
ancho = float(input("Enter width of the rectangle: "))
area_rectangulo = longitud * ancho  # Fórmula del área
perimetro_rectangulo = 2 * (longitud + ancho)  # Fórmula del perímetro
print("The area of the rectangle is", area_rectangulo)
print("The perimeter of the rectangle is", perimetro_rectangulo)

# Ejercicio 7: Calcular el área y circunferencia de un círculo
radio = float(input("Enter radius of the circle: "))
area_circulo = 3.14 * radio * radio  # Fórmula del área
circunferencia_circulo = 2 * 3.14 * radio  # Fórmula de la circunferencia
print("The area of the circle is", area_circulo)
print("The circumference of the circle is", circunferencia_circulo)

# Ejercicio 8: Calcular pendiente, intersección con el eje x y eje y de y = 2x - 2
# La pendiente es el coeficiente de x (en este caso 2)
pendiente = 2  # Pendiente de la recta
interseccion_y = -2  # Intersección con el eje y
interseccion_x = 2  # Intersección con el eje x
print("The slope is", pendiente)
print("The x-intercept is", interseccion_x)
print("The y-intercept is", interseccion_y)

# Ejercicio 9: Calcular la pendiente y la distancia euclidiana entre dos puntos
# Fórmulas de la pendiente y distancia euclidiana
punto1_x = 2
punto1_y = 2
punto2_x = 6
punto2_y = 10
pendiente_puntos = (punto2_y - punto1_y) / (punto2_x - punto1_x)  # Fórmula de la pendiente
distancia_euclidiana = ((punto2_x - punto1_x)**2 + (punto2_y - punto1_y)**2)**0.5  # Fórmula de la distancia euclidiana
print("The slope between the points is", pendiente_puntos)
print("The Euclidean distance between the points is", distancia_euclidiana)

# Ejercicio 10: Comparar pendientes
pendiente_1 = 2
pendiente_2 = pendiente_puntos
print("Are the slopes equal?", pendiente_1 == pendiente_2)

# Ejercicio 11: Calcular el valor de y para diferentes valores de x en y = x^2 + 6x + 9
x_0 = 0
x_1 = 1
x_2 = -1
x_3 = 2
x_4 = -2

# Calculamos los valores de y
y_0 = x_0**2 + 6*x_0 + 9
y_1 = x_1**2 + 6*x_1 + 9
y_2 = x_2**2 + 6*x_2 + 9
y_3 = x_3**2 + 6*x_3 + 9
y_4 = x_4**2 + 6*x_4 + 9

print("For x = 0, y =", y_0)
print("For x = 1, y =", y_1)
print("For x = -1, y =", y_2)
print("For x = 2, y =", y_3)
print("For x = -2, y =", y_4)

# Ejercicio 12: Longitud de 'python' y 'dragon', y afirmación falsa
longitud_python = len("python")
longitud_dragon = len("dragon")
print("Longitud de 'python':", longitud_python)
print("Longitud de 'dragon':", longitud_dragon)
print("Is the length of 'python' equal to the length of 'dragon'?", longitud_python == longitud_dragon)

# Ejercicio 13: Comprobar si 'on' está en 'python' y 'dragon' con operador and
print("Is 'on' in 'python' and 'dragon'?", 'on' in "python" and 'on' in "dragon")

# Ejercicio 14: Comprobar si 'jargon' está en la oración
oracion = "Espero que este curso no esté lleno de jerga"
print("Is 'jargon' in the sentence?", 'jargon' in oracion)

# Ejercicio 15: Longitud de 'python', convertir a float y luego a string
longitud_python_float = float(longitud_python)
longitud_python_str = str(longitud_python_float)
print("Longitud de 'python' convertida a string:", longitud_python_str)

# Ejercicio 16: Comprobar si un número es par
numero = 4
es_par = numero % 2 == 0
print("Es", numero, "par?", es_par)

# Ejercicio 17: Comparar la división de piso de 7 por 3 con el valor entero de 2.7
div_piso = 7 // 3
valor_entero = int(2.7)
print("Is the floor division of 7 by 3 equal to int(2.7)?", div_piso == valor_entero)

# Ejercicio 18: Comparar el tipo de '10' con el tipo de 10
print("Is type of '10' equal to type of 10?", type("10") == type(10))

# Ejercicio 19: Comprobar si int('9.8') es igual a 10
print("Is int('9.8') equal to 10?", int(9.8) == 10)

# Ejercicio 20: Calcular salario semanal de una persona
horas = float(input("Enter hours: "))
tarifa = float(input("Enter rate per hour: "))
salario = horas * tarifa  # Cálculo del salario
print("Your weekly earning is", salario)

# Ejercicio 21: Calcular la cantidad de segundos vividos
años_vividos = float(input("Enter number of years you have lived: "))
segundos_vividos = años_vividos * 365 * 24 * 60 * 60  # Conversión de años a segundos
print("You have lived for", segundos_vividos, "seconds.")

# Ejercicio 22: Imprimir una tabla con valores
# En lugar de usar un bucle, lo haremos manualmente
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
