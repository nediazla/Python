import time
# pip install datetime en terminal de pycharm o de windows
from datetime import datetime, timedelta

# Diccionario para almacenar las tareas
tareas = {}


# 1. Función para agregar una tarea
def agregar_tarea(tareas, tarea, prioridad):
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tareas[tarea] = {"prioridad": prioridad, "fecha_agregado": fecha_actual}
    print(f"Tarea '{tarea}' agregada con prioridad {prioridad}.")


# 2. Función para eliminar una tarea
def eliminar_tarea(tareas, tarea):
    if tarea in tareas:
        del tareas[tarea]
        print(f"Tarea '{tarea}' eliminada.")
    else:
        print(f"Tarea '{tarea}' no encontrada.")


# 3. Función para modificar una tarea (prioridad o nombre)
def modificar_tarea(tareas, tarea, nueva_prioridad=None, nuevo_nombre=None):
    if tarea in tareas:
        if nueva_prioridad:
            tareas[tarea]["prioridad"] = nueva_prioridad
        if nuevo_nombre:
            tareas[nuevo_nombre] = tareas.pop(tarea)
        print(f"Tarea '{tarea}' modificada.")
    else:
        print(f"Tarea '{tarea}' no encontrada.")


# 4. Función para ver todas las tareas
def ver_tareas(tareas):
    if not tareas:
        print("No hay tareas.")
    else:
        print("\nLista de tareas:")
        for tarea, detalles in tareas.items():
            print(
                f"Tarea: {tarea}, Prioridad: {detalles['prioridad']}, Fecha de Agregado: {detalles['fecha_agregado']}")


# 5. Función para ver tareas con alta prioridad
def ver_tareas_alta_prioridad(tareas):
    alta_prioridad = list(filter(lambda t: t[1]["prioridad"] == "Alta", tareas.items()))
    if alta_prioridad:
        print("\nTareas con alta prioridad:")
        for tarea, detalles in alta_prioridad:
            print(
                f"Tarea: {tarea}, Prioridad: {detalles['prioridad']}, Fecha de Agregado: {detalles['fecha_agregado']}")
    else:
        print("\nNo hay tareas con alta prioridad.")


# 6. Función para verificar el tiempo restante
def tiempo_restante(tiempo_inicio, tiempo_limite):
    tiempo_actual = datetime.now()
    tiempo_pasado = tiempo_actual - tiempo_inicio
    tiempo_restante = tiempo_limite - tiempo_actual  # Devolver la diferencia entre tiempo límite y tiempo actual
    return tiempo_restante


# 7. Función para mostrar el tiempo restante de manera legible
def mostrar_tiempo_restante(tiempo_restante):
    # Asegurarnos de que estamos trabajando con un objeto timedelta
    if isinstance(tiempo_restante, timedelta):
        total_segundos = int(tiempo_restante.total_seconds())  # Total de segundos
        minutos, segundos = divmod(total_segundos, 60)  # Dividir entre 60 para obtener minutos y segundos
        print(f"Tiempo restante: {minutos} minutos y {segundos} segundos")
    else:
        print("Error: El objeto 'tiempo_restante' no es un timedelta.")


# 8. Función para calcular el tiempo que tarda en realizarse una tarea
def realizar_tarea(tarea):
    print(f"Realizando la tarea: {tarea}...")
    time.sleep(2)  # Simula el tiempo que lleva completar la tarea
    print(f"Tarea '{tarea}' completada.")


# 9. Función para jugar el juego
def jugar():
    print("Bienvenido al juego 'Administrador de Tareas del Día'!")
    print("Tu objetivo es organizar y realizar tus tareas antes de que se acabe el tiempo.")

    # Tiempo límite para el juego (5 minutos)
    tiempo_inicio = datetime.now()
    tiempo_limite = tiempo_inicio + timedelta(minutes=5)

    while True:
        # Mostrar tiempo restante
        tiempo_restante_actual = tiempo_restante(tiempo_inicio, tiempo_limite)
        mostrar_tiempo_restante(tiempo_restante_actual)

        if tiempo_restante_actual.total_seconds() <= 0:
            print("¡El tiempo se ha agotado! Has perdido el juego.")
            break

        # Menú de opciones
        print("\nOpciones disponibles:")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Modificar tarea")
        print("4. Ver todas las tareas")
        print("5. Ver tareas de alta prioridad")
        print("6. Realizar tarea")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            tarea = input("Introduce el nombre de la tarea: ")
            prioridad = input("Introduce la prioridad (Alta/Baja): ")
            agregar_tarea(tareas, tarea, prioridad)
        elif opcion == "2":
            tarea = input("Introduce el nombre de la tarea a eliminar: ")
            eliminar_tarea(tareas, tarea)
        elif opcion == "3":
            tarea = input("Introduce el nombre de la tarea a modificar: ")
            nueva_prioridad = input("Introduce la nueva prioridad (Alta/Baja): ")
            nuevo_nombre = input("Introduce el nuevo nombre de la tarea: ")
            modificar_tarea(tareas, tarea, nueva_prioridad, nuevo_nombre)
        elif opcion == "4":
            ver_tareas(tareas)
        elif opcion == "5":
            ver_tareas_alta_prioridad(tareas)
        elif opcion == "6":
            if not tareas:
                print("No hay tareas disponibles para realizar.")
            else:
                tarea = input("Introduce el nombre de la tarea a realizar: ")
                if tarea in tareas:
                    realizar_tarea(tarea)
                    eliminar_tarea(tareas, tarea)  # Al realizar la tarea, se elimina
                else:
                    print(f"Tarea '{tarea}' no encontrada.")
        elif opcion == "7":
            print("¡Gracias por jugar! ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Por favor elige una opción correcta.")


# 10. Ejecutar el juego
if __name__ == "__main__":
    jugar()
