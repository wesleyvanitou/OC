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
        self.guardian = None

    def load(self, filename):
        """ Maze file loader"""

        with open(filename) as F:
            for x, row in enumerate(F):
                for y, col in enumerate(row):
                    coordinates = (x, y)
                    if col in ".PG":
                        self.path.append(coordinates)
                        if col in "P":
                            self.player = coordinates
                        if col in "G":
                            self.guardian = coordinates
                    else:
                        self.wall.append(coordinates)
        return self.path, self.wall, self.player, self.guardian

    def items(self, number=3, i=0):
        """ This function will select 3 coordinates for the
        items exlcuding the player and guardian"""

        item = "needle syringe tube".split()

        loc = sample([
            i for i in self.path
            if i not in [self.player, self.guardian]], k=number)

        for a, b in zip(loc, item):
            self.item[a] = b
        
        return self.item

#maze = Maze()
#maze.load('labyrinth.txt')
#print("paths\n", maze.path, "\n")
#print("Player:\n", maze.player)
#print("Guardian:\n", maze.guardian)
#print("Items:\n", maze.items())
