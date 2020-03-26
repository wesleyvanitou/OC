# -*- coding: utf-8 -*-

#+++++++++IMPORT++++++++++

# Standard libraries

# Third party
import pygame

# Local applications
from pkg import maze

#+++++++++++++++++++++++++

#maze = Maze("pkg/labyrinth.txt")

""" THis file contains all the game assets"""

# Design
SPRITE = 20

SCREEN =\
SURFACE = ((maze.size[0] + 1) * SPRITE, (maze.size[1] + 1) * SPRITE)

# Assets
# Characters
HERO = "i/MacGyver.png"
GUARD = "i/Gardien.png"

# Items
ITEM_SIZE = (20, 20)

NEEDLE = "i/aiguille.png"
TUBE = "i/tube_plastique.png"
SYRINGE = "i/seringue.png"

PATH = "i/path.png"
WALL = "i/wall.png"
