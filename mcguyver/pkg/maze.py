# -*- coding: utf-8 -*-

from random import sample

class Maze:
    """This class will contains all the parameters
    of the maze"""

    def __init__(self):
        """ Initialize the attributes"""
        self.paths = []
        self.walls = []
        self.items = {}
        self.player = None
        self.guardian = None

    def load(self, filename):
        """ Maze file loader"""

        with open(filename) as F:
            for x, row in enumerate(F):
                for y, col in enumerate(row):
                    coordinates = (x, y)
                    if col in ".PG":
                        self.paths.append(coordinates)
                        if col in "P":
                            self.player = coordinates
                        if col in "G":
                            self.guardian = coordinates
                    else:
                        self.walls.append(coordinates)
        return self.paths, self.walls, self.player, self.guardian

    def set_items(self, number=3, i=0):
        """ This function will select 3 coordinates for the
        items exlcuding the player and guardian"""
        items_loc = sample([
            i for i in self.paths
            if i not in [self.player, self.guardian]], k=number)

        for i, loc in enumerate(items_loc):
            for item in "needle, tube, syringe".split():
                self.items[item] = items_loc[i]
                i = i - 1
#        while i < number:
#            for x in items_loc:
#                for item in "needle, tube, syringe".split():
#                    self.items[i] = (item, items_loc[i])
#            i = i + 1
        return self.items

maze = Maze()
maze.load('labyrinth.txt')
print("paths\n", maze.paths, "\n")
print("Player:\n", maze.player)
print("Guardian:\n", maze.guardian)
print("Items:\n", maze.set_items())
