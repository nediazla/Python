# Solicita al usuario el número de miembros de la familia
miembros = int(input("Cuantos miembros tiene tu familia? - "))

# Se crean tres listas vacías para almacenar nombres, edades y relaciones de los miembros
nombres = []
edades = []
relaciones = []

# Se utiliza un ciclo para pedir el nombre de cada miembro y añadirlo a la lista 'nombres'
for i in range(miembros):
    nombre = input(f"Introduce el nombre del miembro {i + 1}: ")
    nombres.append(nombre)

# Otro ciclo para pedir la edad de cada miembro de la familia y añadirla a la lista 'edades'
for i in range(miembros):
    edad = int(input(f"Cuantos anos tiene {nombres[i]}? - "))
    edades.append(edad)

# Otro ciclo para pedir la relación de cada miembro dentro de la familia y añadirla a la lista 'relaciones'
for i in range(miembros):
    relacion = input(f"Cual es la relacion de {nombres[i]} dentro de la familia? - ")
    relaciones.append(relacion)

# Calcula el promedio de edad sumando todas las edades y dividiendo entre el número de miembros
promedio_edad = sum(edades) / miembros

# Encuentra la edad mayor de la lista de edades
edad_mayor = max(edades)
# Encuentra la edad menor de la lista de edades
edad_menor = min(edades)

# Encuentra el nombre de la persona con la edad mayor
nombre_mayor = nombres[edades.index(edad_mayor)]
# Encuentra el nombre de la persona con la edad menor
nombre_menor = nombres[edades.index(edad_menor)]

# Imprime la información sobre los miembros de la familia
print("\nLos miembros de  tu familia son:")
for i in range(miembros):
    print(f"{nombres[i]}, es el {relaciones[i]} y tiene {edades[i]} anos.")

# Imprime el promedio de la edad de la familia con dos decimales
print(f"\nEl promedio de edad de la familia es de: {promedio_edad:.2f} anos")
# Imprime el nombre de la persona más mayor y su edad
print(f"\nLa persona con la edad mayor es {nombre_mayor} con {edad_mayor} anos")
# Imprime el nombre de la persona más joven y su edad
print(f"La persona con la edad menor es {nombre_menor} con {edad_menor} anos")
