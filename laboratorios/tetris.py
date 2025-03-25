import tkinter as tk
import random

class Tetris:
    def __init__(self, root):
        # Inicialización de la ventana principal del juego
        self.root = root
        self.root.title("Tetris")  # Título de la ventana

        # Definimos el tamaño de la ventana
        self.width = 300  # Ancho de la ventana
        self.height = 600  # Alto de la ventana
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg='black')
        self.canvas.pack()

        # Definir el tamaño de las celdas y el tablero
        self.cell_size = 30  # Tamaño de cada celda en el tablero
        self.rows = self.height // self.cell_size  # Número de filas en el tablero
        self.cols = self.width // self.cell_size  # Número de columnas en el tablero

        # Tetris Shapes (Las 7 figuras de Tetris)
        self.shapes = [
            [(0, 1), (1, 1), (2, 1), (3, 1)],  # I
            [(0, 0), (1, 0), (2, 0), (2, 1)],  # J
            [(0, 1), (1, 1), (2, 0), (2, 1)],  # L
            [(0, 0), (0, 1), (1, 0), (1, 1)],  # O
            [(1, 0), (2, 0), (0, 1), (1, 1)],  # S
            [(0, 0), (1, 0), (2, 0), (1, 1)],  # T
            [(1, 0), (2, 0), (0, 1), (1, 1)],  # Z
        ]

        # El tablero donde se guardan las piezas fijas (estado del juego)
        self.board = [[0] * self.cols for _ in range(self.rows)]

        # Pieza actual
        self.current_shape = None  # Al principio no hay pieza
        self.current_position = (0, 0)  # La pieza comienza en la posición (0, 0)

        # Llamamos a la función para iniciar el juego
        self.start_game()

        # Control de teclas (movimientos y rotación)
        self.root.bind("<Left>", self.move_left)  # Movimiento hacia la izquierda
        self.root.bind("<Right>", self.move_right)  # Movimiento hacia la derecha
        self.root.bind("<Down>", self.move_down)  # Movimiento hacia abajo
        self.root.bind("<Up>", self.rotate)  # Rotación de la pieza

    def start_game(self):
        # Inicia el juego generando una nueva pieza y comenzando el ciclo del juego
        self.new_piece()  # Genera una nueva pieza
        self.game_loop()  # Inicia el ciclo de juego

    def new_piece(self):
        # Selecciona una pieza aleatoria y la coloca en la posición inicial
        self.current_shape = random.choice(self.shapes)
        self.current_position = (self.cols // 2 - 1, 0)  # Posición inicial en el centro superior del tablero

    def move_left(self, event=None):
        # Verificamos si la pieza puede moverse a la izquierda
        new_position = (self.current_position[0] - 1, self.current_position[1])
        if not self.collides(new_position, self.current_shape):  # Si no hay colisión
            self.current_position = new_position
        self.redraw()  # Redibujamos el tablero

    def move_right(self, event=None):
        # Verificamos si la pieza puede moverse a la derecha
        new_position = (self.current_position[0] + 1, self.current_position[1])
        if not self.collides(new_position, self.current_shape):  # Si no hay colisión
            self.current_position = new_position
        self.redraw()  # Redibujamos el tablero

    def move_down(self, event=None):
        # Verificamos si la pieza puede moverse hacia abajo
        new_position = (self.current_position[0], self.current_position[1] + 1)
        if not self.collides(new_position, self.current_shape):  # Si no hay colisión
            self.current_position = new_position
        else:
            # Si la pieza no puede moverse, se fija en el tablero y generamos una nueva pieza
            self.lock_piece()
            self.new_piece()
        self.redraw()  # Redibujamos el tablero

    def rotate(self, event=None):
        # Rotamos la pieza 90 grados
        rotated_shape = [(y, -x) for x, y in self.current_shape]
        if not self.collides(self.current_position, rotated_shape):  # Verificamos si la rotación es válida
            self.current_shape = rotated_shape
        self.redraw()  # Redibujamos el tablero

    def collides(self, position, shape):
        # Verifica si la pieza en la posición indicada colisiona con otras piezas o con los bordes del tablero
        for x, y in shape:
            board_x = position[0] + x
            board_y = position[1] + y
            if not (0 <= board_x < self.cols and 0 <= board_y < self.rows) or self.board[board_y][board_x] != 0:
                return True  # Hay colisión
        return False  # No hay colisión

    def lock_piece(self):
        # Fija la pieza al tablero (la convierte en una pieza fija)
        for x, y in self.current_shape:
            board_x = self.current_position[0] + x
            board_y = self.current_position[1] + y
            self.board[board_y][board_x] = 1  # Marcamos la celda como ocupada
        self.clear_lines()  # Llamamos para limpiar las líneas completas

    def clear_lines(self):
        # Revisa si alguna línea está completa y la elimina
        for y in range(self.rows):
            if all(self.board[y][x] != 0 for x in range(self.cols)):  # Si la línea está completa
                self.board.pop(y)  # Eliminamos la línea
                self.board.insert(0, [0] * self.cols)  # Insertamos una nueva línea vacía al principio

    def redraw(self):
        # Limpiamos la pantalla
        self.canvas.delete("all")

        # Dibujamos las piezas fijas en el tablero
        for y in range(self.rows):
            for x in range(self.cols):
                if self.board[y][x] != 0:  # Si la celda está ocupada por una pieza fija
                    self.canvas.create_rectangle(
                        x * self.cell_size, y * self.cell_size,
                        (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                        fill='gray', outline='black'
                    )

        # Dibujamos la pieza actual
        for x, y in self.current_shape:
            self.canvas.create_rectangle(
                (self.current_position[0] + x) * self.cell_size,
                (self.current_position[1] + y) * self.cell_size,
                (self.current_position[0] + x + 1) * self.cell_size,
                (self.current_position[1] + y + 1) * self.cell_size,
                fill='blue', outline='black'
            )

    def game_loop(self):
        # Mueve la pieza hacia abajo automáticamente en cada ciclo del juego
        self.move_down()
        self.root.after(500, self.game_loop)  # Vuelve a llamar a game_loop después de 500ms

# Crear la ventana de la aplicación Tkinter
root = tk.Tk()
game = Tetris(root)  # Crea una instancia del juego
root.mainloop()  # Inicia el bucle principal de la interfaz gráfica

# cosas a agregar: puntaje, perder