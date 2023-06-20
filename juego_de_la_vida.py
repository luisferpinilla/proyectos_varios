import tkinter as tk
import random
import time


class GameOfLife:
    def __init__(self, width, height, cell_size=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cells = [[random.randint(0, 1) for _ in range(width)]
                      for _ in range(height)]
        self.generation = 0

        self.root = tk.Tk()
        self.canvas = tk.Canvas(
            self.root, width=width*cell_size, height=height*cell_size)
        self.canvas.pack()
        self.root.title("Game of Life")
        self.root.bind("<space>", self.toggle_running)
        self.running = False

        self.draw_cells()
        self.root.after(1000, self.update_generation)
        self.root.mainloop()

    def draw_cells(self):
        self.canvas.delete("all")
        for y in range(self.height):
            for x in range(self.width):
                if self.cells[y][x]:
                    x1 = x * self.cell_size
                    y1 = y * self.cell_size
                    x2 = x1 + self.cell_size
                    y2 = y1 + self.cell_size
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")

    def update_generation(self):
        if self.running:
            new_cells = [[0 for _ in range(self.width)]
                         for _ in range(self.height)]
            for y in range(self.height):
                for x in range(self.width):
                    neighbors = self.count_neighbors(x, y)
                    if self.cells[y][x] and neighbors in [2, 3]:
                        new_cells[y][x] = 1
                    elif not self.cells[y][x] and neighbors == 3:
                        new_cells[y][x] = 1
            self.cells = new_cells
            self.generation += 1
            self.draw_cells()
        self.root.after(100, self.update_generation)

    def count_neighbors(self, x, y):
        count = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                nx = (x + dx + self.width) % self.width
                ny = (y + dy + self.height) % self.height
                count += self.cells[ny][nx]
        return count

    def toggle_running(self, event):
        self.running = not self.running


# Iniciar el juego con una cuadrícula de 50x50 y tamaño de celda de 10 píxeles
game = GameOfLife(100, 100, 10)
