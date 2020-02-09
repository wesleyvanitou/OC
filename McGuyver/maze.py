from random import sample

class Maze:

    def __init__(self):
        self.player = []
        self.guardian = []
        self.paths = []
        self.walls = []
        self.items = "3"

    def grid(self):
        """ Generate the coordinates of the grid elements"""
        with open('grid') as grid: # Open grid file as var grid
            grid = grid.readlines()

            # Search for the x, y coordinates for the path

        for n_lines, lines in enumerate(grid):
            for  n_col, colunms in enumerate(lines):
                if colunms == "S":
                    self.player.append((n_lines, n_col))
                elif colunms == "G":
                    self.guardian.append((n_lines, n_col))
                elif colunms == ".":
                    self.paths.append((n_lines, n_col))
                else:
                    self.walls.append((n_lines, n_col))

        # Set 3 random place for the items
        xy_items = sample(self.paths, k=3)


