# -*- coding: utf-8 -*-

#+++++++++IMPORT++++++++++

# Standard libraries


# Third party
import pygame

# Local applications
from pkg import config as cfg, maze
#+++++++++++++++++++++++++

class Guard(pygame.sprite.Sprite):
    """ This class defines the visual
    carastetictics of Mac Guyver"""

    def __init__(self):
        self.maze = maze
        super().__init__() # Superclass constructor

        self.img = pygame.transform.scale(
            pygame.image.load(cfg.GUARD), cfg.ITEM_SIZE)

        self.rect = self.img.get_rect()
        self.rect.x = maze.guard[0] * cfg.SPRITE
        self.rect.y = maze.guard[1] * cfg.SPRITE



#class Behavior:
#    """Constructor"""
#
#    def __init__(self):
#        """Constructor"""
#        self.maze = maze
#        self.locate = \
#        self.initial = maze.hero
#        self.grab = []
#        self.joystick = None
#        self.pressed = {}
