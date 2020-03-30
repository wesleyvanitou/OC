# -*- coding: utf-8 -*-

"""This is the maze generattor."""

#+++++++++IMPORT++++++++++

# Standard libraries
from random import sample

# Third party
# Local applications
from .config import NB_ITEMS
#+++++++++++++++++++++++++

class Maze:
    """This class will contains all the parameters
    of the maze"""

    def __init__(self, filename):
        """ Constructor"""
        self.size = None
        self.hero = None
        self.guard = None
        self.path = []
        self.wall = []
        self.lab = []
        self.item = {}
        self._load(filename)
        self._items()

    def _load(self, filename):
        "Maze file loader"""

        with open(filename) as labyrinth:
            for y, row in enumerate(labyrinth):
                for x, col in enumerate(row.strip()):
                    self.size = (x, y)
                    if col in ".PG":
                        self.path.append(self.size)
                        if col in "P":
                            self.hero = self.size
                        if col in "G":
                            self.guard = self.size
                    else:
                        self.wall.append(self.size)

    def _items(self):
        """ This function will select 3 coordinates for the
        items exlcuding the player and guard"""

        itemlist = "needle syringe tube".split()

        location = sample([
            i for i in self.path
            if i not in [self.hero, self.guard]], k=NB_ITEMS)

        for key, value in zip(itemlist, location):
            self.item[value] = key



# File test
#maze = Maze("settings/maze.txt")
#x, y = maze.size
#print(maze.guard)
#print(maze.item)
#for key in maze.item:
#    print(key[1])
#for k in maze.item:
#    print(maze.item[k][0], maze.item[k][1])
#
#for k in ("1", "2", "3"):
#    print(k)

