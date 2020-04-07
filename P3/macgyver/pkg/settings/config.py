"""Stores all the preferences settings for the game"""

# -*- coding: utf-8 -*-

# +++++++++IMPORT++++++++++

# Standard libraries

# Third party
import pygame
# Local applications
# +++++++++++++++++++++++++


# Sprite Size
SPR_X, SPR_Y = 20, 20
SPR = (SPR_X, SPR_Y)

MAZES = "pkg/settings/mazes/01.txt"

# Characters
HERO = "pkg/sprites/i/characters/macgyver.png"
GUARD = "pkg/sprites/i/characters/guardian.png"

# Items
ITEM_SIZE = (SPR_X, SPR_Y)
NB_ITEMS = 3

ITEMS = "pkg/sprites/i/items/{}.png"
ITEMSDIR = "pkg/sprites/i/items"
# Background

TILES = pygame.image.load(
    "pkg/sprites/i/background/tiles.png")

WIN = pygame.image.load(
    "pkg/sprites/i/display/win.gif")

GAMEOVER = pygame.image.load(
    "pkg/sprites/i/display/quit.png")


def tiles(x, y):
    """ Return the desire tile's offset coordinates'"""
    offset = pygame.Rect((x * SPR_X, y * SPR_Y), SPR)
    return offset
