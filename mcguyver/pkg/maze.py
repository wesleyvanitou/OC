# -*- coding: utf-8 -*-

from random import sample


class Maze:
    """This class will contains all the parameters
    of the maze"""

    def __init__(self):
        """ Constructor"""
        self.path = []
        self.wall = []
        self.item = {}
        self.player = None
        self.guard = None

    def load(self, filename):
        "Maze file loader"""

        with open(filename) as labyrinth:
            for x, row in enumerate(labyrinth):
                for y, col in enumerate(row):
                    coordinates = (x, y)
                    if col in ".PG":
                        self.path.append(coordinates)
                        if col in "P":
                            self.player = coordinates
                        if col in "G":
                            self.guard = coordinates
                    else:
                        self.wall.append(coordinates)
        return self.path, self.wall, self.player, self.guard

    def items(self, number=3):
        """ This function will select 3 coordinates for the
        items exlcuding the player and guard"""

        item = "needle syringe tube".split()

        loc = sample([
            i for i in self.path
            if i not in [self.player, self.guard]], k=number)

        for key, value in zip(loc, item):
            self.item[key] = value

        return self.item
