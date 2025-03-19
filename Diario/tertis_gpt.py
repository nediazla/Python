import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 300
ALTO = 600
TAM_CELDA = 30
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tetris")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
NARANJA = (255, 165, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
CIAN = (0, 255, 255)
MORADO = (128, 0, 128)
AMARILLO = (255, 255, 0)

# Definir las formas de las piezas de Tetris
PIEZAS = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]],  # L
]

COLORES_PIEZAS = [AZUL, NARANJA, ROJO, VERDE, CIAN, MORADO, AMARILLO]

# Función para dibujar una pieza en el tablero
def dibujar_pieza(pieza, color, x, y):
    for i, fila in enumerate(pieza):
        for j, bloque in enumerate(fila):
            if bloque:
                pygame.draw.rect(PANTALLA, color, (x + j * TAM_CELDA, y + i * TAM_CELDA, TAM_CELDA, TAM_CELDA))

# Función para dibujar el tablero
def dibujar_tablero():
    PANTALLA.fill(NEGRO)
    for x in range(0, ANCHO, TAM_CELDA):
        for y in range(0, ALTO, TAM_CELDA):
            pygame.draw.rect(PANTALLA, BLANCO, (x, y, TAM_CELDA, TAM_CELDA), 1)

# Función principal para crear un juego básico de Tetris
def juego():
    reloj = pygame.time.Clock()
    corriendo = True

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        # Dibujar el tablero y las piezas
        dibujar_tablero()

        # Generar una pieza aleatoria y dibujarla en la parte superior
        pieza_idx = random.randint(0, len(PIEZAS) - 1)
        pieza = PIEZAS[pieza_idx]
        color = COLORES_PIEZAS[pieza_idx]
        dibujar_pieza(pieza, color, 120, 0)  # Ubicamos la pieza en la parte superior del tablero

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad del juego
        reloj.tick(10)

    pygame.quit()

# Iniciar el juego
juego()
