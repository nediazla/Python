# Materias fijas para todos los estudiantes
MATERIAS = ['Historia', 'Español', 'Matemáticas', 'Informática']

# Función para agregar un estudiante y sus calificaciones
def agregar_estudiante(estudiantes):
    # Pedimos el nombre del estudiante
    nombre = input('Agregue nombre del Estudiante: ')

    # Creamos un diccionario para almacenar las materias con sus calificaciones
    materias = {materia: [] for materia in MATERIAS}

    # Bucle para ingresar las calificaciones de cada materia
    for materia in MATERIAS:
        # Pedimos la cantidad de calificaciones para cada materia
        cantidad_calificaciones = int(input(f'Ingrese la cantidad de calificaciones para {materia} de {nombre}: '))

        # Bucle para ingresar cada calificación
        for i in range(cantidad_calificaciones):
            calificacion = float(input(f'Ingrese la calificación {i + 1} para {materia}: '))
            materias[materia].append(calificacion)

    # Guardamos las materias y calificaciones del estudiante en el diccionario 'estudiantes'
    estudiantes[nombre] = materias

    # Mensaje de confirmación
    print(f'Estudiante {nombre} ha sido agregado con éxito')


# Función para calcular el promedio de las calificaciones de un estudiante
def calcular_promedio(materias):
    # Calculamos el promedio de todas las calificaciones de las materias
    total_calificaciones = sum(sum(calificaciones) for calificaciones in materias.values())
    total_materias = sum(len(calificaciones) for calificaciones in materias.values())

    return total_calificaciones / total_materias if total_materias else 0


# Función que determina el estado de aprobación de cada materia
def estado_materia(calificaciones):
    # Si el promedio de las calificaciones es mayor o igual a 7, la materia está aprobada
    promedio = sum(calificaciones) / len(calificaciones) if calificaciones else 0
    return "Aprobado" if promedio >= 7 else "Reprobado"


# Función que determina el estado del estudiante basado en su promedio total
def estado_estudiante(promedio):
    # Si el promedio total es mayor o igual a 7, el estudiante está aprobado
    return "Aprobado" if promedio >= 7 else "Reprobado"


# Función que muestra la información de todos los estudiantes
def mostrar_estudiantes(estudiantes):
    # Verificamos si hay estudiantes en el diccionario
    if estudiantes:
        # Iteramos sobre el diccionario de estudiantes
        for nombre, materias in estudiantes.items():
            # Calculamos el promedio de las calificaciones del estudiante
            promedio = calcular_promedio(materias)

            # Mostramos el nombre, promedio y estado del estudiante
            print(f'\n{nombre}: Promedio Total = {promedio:.2f}, Estado = {estado_estudiante(promedio)}')

            # Mostramos el estado de cada materia
            for materia, calificaciones in materias.items():
                print(f'{materia}: Calificaciones = {calificaciones}, Estado = {estado_materia(calificaciones)}')
    else:
        # Si no hay estudiantes, mostramos un mensaje indicando que no hay datos
        print('No hay estudiantes')


# Función para obtener el top 3 de los mejores estudiantes
def top_3_estudiantes(estudiantes):
    # Creamos una lista de tuplas con el nombre del estudiante y su promedio
    promedios = [(nombre, calcular_promedio(materias)) for nombre, materias in estudiantes.items()]

    # Ordenamos la lista por promedio de mayor a menor
    promedios.sort(key=lambda x: x[1], reverse=True)

    # Mostramos el top 3 de estudiantes
    print("\nTop 3 de los mejores estudiantes:")
    for i in range(min(3, len(promedios))):
        nombre, promedio = promedios[i]
        print(f'{i + 1}. {nombre}: Promedio = {promedio:.2f}')


# Función principal que maneja el menú del programa
def main():
    # Creamos un diccionario vacío para almacenar los estudiantes
    estudiantes = {}

    while True:
        # Imprimimos las opciones del menú
        print('\nMenu:')
        print('1. Agregar Estudiante')
        print('2. Ver Estudiantes')
        print('3. Ver Top 3 Estudiantes')
        print('4. Salir')

        # Pedimos al usuario seleccionar una opción
        opcion = input('Seleccione una opción: ')

        # Dependiendo de la opción elegida, ejecutamos una acción
        if opcion == '1':
            # Llamamos a la función para agregar un estudiante
            agregar_estudiante(estudiantes)
        elif opcion == '2':
            # Llamamos a la función para mostrar todos los estudiantes
            mostrar_estudiantes(estudiantes)
        elif opcion == '3':
            # Llamamos a la función para mostrar el top 3 de estudiantes
            top_3_estudiantes(estudiantes)
        elif opcion == '4':
            # Salimos del bucle y terminamos el programa
            print('Saliendo')
            break
        else:
            # Si la opción no es válida, mostramos un mensaje de error
            print('Ingrese una opción válida, opciones (1, 2, 3, 4)')


# Punto de entrada del programa
if __name__ == "__main__":
    # Ejecutamos la función principal
    main()
