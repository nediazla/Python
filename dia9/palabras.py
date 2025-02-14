import random

# Lista de palabras posibles
palabras = ['python', 'programacion', 'desarrollador', 'computadora', 'algoritmo', 'juego']

# Elegir una palabra al azar
palabra_secreta = random.choice(palabras)

# Convertir la palabra secreta en una lista de guiones para mostrarla al jugador
palabra_oculta = ['_'] * len(palabra_secreta)

# Número de intentos
intentos = 6

print("¡Bienvenido al juego de Adivina la palabra!")
print("Tienes que adivinar la palabra secreta.")
print("La palabra tiene", len(palabra_secreta), "letras.")
print(" ".join(palabra_oculta))
print()

# Bucle principal del juego
while intentos > 0:
    # Solicitar al jugador una letra
    letra = input(f"Tienes {intentos} intentos restantes. Introduce una letra: ").lower()

    # Validar si el jugador introduce una sola letra
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, ingresa una sola letra.")
        continue

    # Verificar si la letra está en la palabra secreta
    if letra in palabra_secreta:
        print(f"¡Correcto! La letra '{letra}' está en la palabra.")
        # Reemplazar los guiones por la letra en las posiciones correspondientes
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                palabra_oculta[i] = letra
    else:
        intentos -= 1
        print(f"¡Incorrecto! La letra '{letra}' no está en la palabra.")

    # Mostrar el progreso del jugador
    print(" ".join(palabra_oculta))

    # Comprobar si el jugador ha adivinado toda la palabra
    if '_' not in palabra_oculta:
        print("¡Felicidades! Has adivinado la palabra:", palabra_secreta)
        break
else:
    print("¡Te has quedado sin intentos! La palabra secreta era:", palabra_secreta)
