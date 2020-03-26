# -*- coding: utf-8 -*-

#+++++++++IMPORT++++++++++

# Standard libraries


# Third party
import pygame

# Local applications
from pkg import config as cfg, maze
#+++++++++++++++++++++++++

class Hero(pygame.sprite.Sprite):
    """ This class defines the visual
    carastetictics of Mac Guyver"""

    def __init__(self):
        super().__init__() # Superclass constructor

        self.img = pygame.transform.scale(
            pygame.image.load(cfg.HERO), cfg.ITEM_SIZE)

        self.rect = self.img.get_rect()
        self.rect.x = maze.hero[0] * cfg.SPRITE
        self.rect.y = maze.hero[1] * cfg.SPRITE


class Behavior:
    """Constructor"""

    def __init__(self):
        """Constructor"""
        self.maze = maze
        self.locate = \
        self.initial = maze.hero
        self.grab = []
        self.joystick = None
        self.pressed = {}

    def controller(self, joystick):
        """This class creates the controller
        for the player base on the VIM Editor
        navigation system:
        h(←), j(↓), k(↑), l(→)"""
        x, y = self.locate
        self.initial = (x, y)
        # Depending of the playe's input, the coordinates will change
        #self.joystick = input("\nMove McGuyver \nh(←), j(↓), k(↑), l(→): ")
#        if self.joystick in "": # if no input, the player don't move
#            self.joystick = (x, y)
#        elif self.joystick is ("h"): # Go Left
#            self.joystick = (x, y - 1)
#        elif self.joystick in "jJ": #Go Down
#            self.joystick = (x + 1, y)
#        elif self.joystick in "kK": #Go Up
#            self.joystick = (x - 1, y)
#        elif self.joystick in "lL": #Go Right
#            self.joystick = (x, y + 1)
        return self.joystick

    def move(self):
        """This method will allows the player to move."""
        if self.joystick in self.maze.path:
            self.locate = self.joystick
            if self.locate in self.maze.item:
                self.grab.append(self.maze.item.pop(self.joystick))
        elif self.joystick in self.maze.wall: #If wall then initial coordinates
            self.locate = self.initial

        return self.locate, self.grab, self.maze.item

