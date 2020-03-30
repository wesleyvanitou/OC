# -*- coding: utf-8 -*-

#+++++++++IMPORT++++++++++

# Standard libraries


# Third party
import pygame
# Local applications
from ..settings import config as cfg, maze
#+++++++++++++++++++++++++


class Hero():
    """Constructor"""

    def __init__(self):
        """Constructor"""
        self.grab = []
        self.stuck = maze.hero

    def controller(self, key, hero):
        """This class creates the controller
        for the player base on the VIM Editor
        navigation system:
        h(←), j(↓), k(↑), l(→)"""
        x, y = hero
        self.stuck = (x, y)
        if key == pygame.K_LEFT:
            moved = (x - 1, y)
        elif key == pygame.K_DOWN:
            moved = (x, y + 1)
        elif key == pygame.K_UP:
            moved = (x, y - 1)
        elif key == pygame.K_RIGHT:
            moved = (x + 1, y)
        return moved

    def move(self, moved):
        """This method will allows the player to move."""
        if moved in maze.path:
            maze.hero = moved
            if maze.hero in maze.item:
                self.grab.append(maze.item.pop(moved))
        elif moved in maze.wall: #If wall then initial coordinates
            maze.hero = self.stuck

        return maze.hero

class HeroSpr(pygame.sprite.Sprite):
    """This class defines the visual
    carastetictics of Mac Guyver"""

    def __init__(self, hero):
        self.hero = hero
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.transform.scale(
            pygame.image.load(cfg.HERO), cfg.ITEM_SIZE)

        x, y = self.hero[0] * cfg.SPR_X, self.hero[1] * cfg.SPR_Y
        self.rect = self.img.get_rect().move(x, y)

    def update(self):
        """Manage the display's update 'of the hero's sprite
        on the screen"""
        x, y = self.hero
        self.rect.x = x * cfg.SPR_X
        self.rect.y = y * cfg.SPR_Y
