# -*- coding: utf-8 -*-

#+++++++++IMPORT++++++++++

# Standard libraries


# Third party
import pygame

# Local applications
from ..settings import config as cfg, maze
#+++++++++++++++++++++++++

class Guard(pygame.sprite.Sprite):
    """ This class defines the visual
    carastetictics of Mac Guyver"""

    def __init__(self):
        super().__init__() # Superclass constructor

        self.img = pygame.transform.scale(
            pygame.image.load(cfg.GUARD), cfg.SPR)

        x, y = maze.guard
        self.rect = self.img.get_rect()
        self.rect.x = x * cfg.SPR_X
        self.rect.y = y * cfg.SPR_Y
