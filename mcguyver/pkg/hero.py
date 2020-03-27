# -*- coding: utf-8 -*-

#+++++++++IMPORT++++++++++

# Standard libraries


# Third party
import pygame
# Local applications
from pkg import config as cfg, maze
#+++++++++++++++++++++++++


class Behavior():
    """Constructor"""

    def __init__(self):
        """Constructor"""
        self.maze = maze
        self.locate = \
        self.initial = maze.hero
        self.grab = []
        self.stuff = 3

    def controller(self, key):
        """This class creates the controller
        for the player base on the VIM Editor
        navigation system:
        h(←), j(↓), k(↑), l(→)"""
        x, y = self.locate
        self.initial = (x, y)
        if key == pygame.K_LEFT:
            moved = (x - 1, y)
        if key == pygame.K_DOWN:
            moved = (x, y + 1)
        if key == pygame.K_UP:
            moved = (x, y - 1)
        if key == pygame.K_RIGHT:
            moved = (x + 1, y)
        return moved

    def move(self, moved):
        """This method will allows the player to move."""
        if moved in self.maze.path:
            self.locate = moved
            if self.locate in self.maze.item:
                self.grab.append(self.maze.item.pop(moved))
        elif moved in self.maze.wall: #If wall then initial coordinates
            self.locate = self.initial

        return self.locate#,self.grab#, self.maze.item

class Hero(pygame.sprite.Sprite, Behavior):
    """ This class defines the visual
    carastetictics of Mac Guyver"""

    def __init__(self):
        super().__init__()
        Behavior.__init__(self)
        self.img = pygame.transform.scale(
            pygame.image.load(cfg.HERO), cfg.ITEM_SIZE)
        self.rect = self.img.get_rect()

#    def update(self):
#        """ Update of the Hero mouvement"""
        x, y = self.locate
        self.rect.x = x * cfg.SPRITE
        self.rect.y = y * cfg.SPRITE
