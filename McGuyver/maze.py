from .assets.grid import G
from random import sample

class Maze:

    def __init__(self):
        self.paths = ""
        self.walls = ""

    def grid(self, grid):
        """test"""
        self.items = "$"

        with open('grid').split() as G:
            G = grid.read().split()
            self.paths = \
            [(x, y) for x, y in enumerate(G) for y, symbol in enumerate(y) if symbol == "."]

            self.walls = \
            [(x, y) for x, y in enumerate(G) for y, symbol in enumerate(y) if symbol == "*"]

        [





    def main():
        Maze.grid()

Maze.main()
