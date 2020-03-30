# -*- coding: utf-8 -*-

#+++++++++IMPORT++++++++++

# Standard libraries


# Third party
import pygame

# Local applications
from ..settings import config as cfg, maze
#+++++++++++++++++++++++++

class Items(pygame.sprite.Sprite):
    # Todo: 
        # The loop doesn't generate the 3 images
        # in the maze. Only the last loop apprear.
        # Find a way to extract the # items.
    def __init__(self):
        super().__init__() # Superclass constructor
        for key, images in zip(maze.item, (cfg.NEEDLE, cfg.SYRINGE, cfg.TUBE)):
            self.img = pygame.transform.scale(
                pygame.image.load(images), cfg.SPR)
            x, y = key
            self.rect = self.img.get_rect()
            self.rect.x = x * cfg.SPR_X
            self.rect.y = y * cfg.SPR_Y
