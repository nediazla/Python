# Función principal
def familia():
    # Pedimos la cantidad de miembros de la familia
    num_miembros = int(input("¿Cuántos miembros tiene tu familia? - "))

    miembros = []  # Lista para almacenar la información de cada miembro
    edades = []  # Lista para almacenar las edades de cada miembro
    mayor = None  # Variable para almacenar el nombre del miembro más mayor
    menor = None  # Variable para almacenar el nombre del miembro más joven
    edad_mayor = -1  # Inicializamos la edad del mayor
    edad_menor = 100  # Inicializamos la edad del menor

    # Pedimos la información de cada miembro
    for i in range(num_miembros):
        print(f"\nMiembro {i + 1}:")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        relacion = input("¿Qué relación tienes con esta persona en la familia? - ")

        miembros.append((nombre, edad, relacion))
        edades.append(edad)

        # Determinamos si esta persona es la más mayor o la más joven
        if edad > edad_mayor:
            edad_mayor = edad
            mayor = nombre

        if edad < edad_menor:
            edad_menor = edad
            menor = nombre

    # Calculamos el promedio de edad
    promedio = sum(edades) / len(edades)

    # Mostramos los resultados
    print("\nResumen:")
    print(f"Promedio de edad de la familia: {promedio:.2f} años")
    print(f"El miembro más mayor es: {mayor} con {edad_mayor} años")
    print(f"El miembro más joven es: {menor} con {edad_menor} años")

    # Listamos los miembros de la familia
    print("\nMiembros de la familia:")
    for miembro in miembros:
        print(f"{miembro[0]} - Edad: {miembro[1]} años - Relación: {miembro[2]}")


# Llamamos a la función
familia()
