import tkinter as tk


class Tetris:
    def __init__(self, root):
        self.root  = root
        self.root.title("Tetris")

        self.width = 300
        self.heigth = 600
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.heigth, bg='black')
        self.canvas.pack()

        self.cell_size = 30
        self.rows = self.heigth // self.cell_size
        self.cols = self.width // self.cell_size

        self.shapes = [
            [(0, 1), (1, 1), (2, 1), (3, 1)],  # I
            [(0, 0), (1, 0), (2, 0), (2, 1)],  # J
            [(0, 1), (1, 1), (2, 0), (2, 1)],  # L
            [(0, 0), (0, 1), (1, 0), (1, 1)],  # O
            [(1, 0), (2, 0), (0, 1), (1, 1)],  # S
            [(0, 0), (1, 0), (2, 0), (1, 1)],  # T
            [(1, 0), (2, 0), (0, 1), (1, 1)],  # Z
        ]

        self.board = [[0] * self.cols for _ in range(self.rows)]

        self.current_shape = None
        self.current_position = (0, 0)

        self.start_game()

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Up>", self.move_up)

def start_game(self)

def new_piece(self)

def move_left

def move_right

def move_down

def move_up

def rotate






root = tk.Tk
game = Tetris(root)
root.mainloop()