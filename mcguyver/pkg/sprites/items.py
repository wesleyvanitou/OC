# -*- coding: utf-8 -*-

#+++++++++IMPORT++++++++++

# Standard libraries


# Third party
import pygame

# Local applications
import config as cfg
#+++++++++++++++++++++++++

class Items(pygame.sprite.Sprite):
    # Todo: 
        # The loop doesn't generate the 3 images
        # in the maze. Only the last loop apprear.
        # Find a way to extract the # items.
    def __init__(self):
        super().__init__() # Superclass constructor
        for key, images in zip(cfg.maze.item, (cfg.NEEDLE, cfg.SYRINGE, cfg.TUBE)):
            self.img = pygame.transform.scale(
                pygame.image.load(images), cfg.ITEM_SIZE)

            self.rect = self.img.get_rect()
            self.rect.x = cfg.maze.item[key][0] * cfg.SPRITE
            self.rect.y = cfg.maze.item[key][1] * cfg.SPRITE
