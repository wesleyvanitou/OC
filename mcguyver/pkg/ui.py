# -*- coding: utf-8 -*-

#+++++++++IMPORT++++++++++

# Standard libraries

# Third party
import pygame

# Local applications
from pkg import maze, config as cfg
from pkg.hero import Hero, Behavior
from pkg.guard import Guard
from pkg.items import Items

#+++++++++++++++++++++++++


class Display:
    """
        Setup of the game's display.

        Here we'll initialize the maze to recuperates all the
        elements necessary to building it.

        Methods
        -------

        The 'game' method creates the visual environement to
        display the game. Not that all the cfg are constants
        located in the 'cfg.py' file.
    """
    def __init__(self):
        """
            Parameters
            ----------

            Maze: Class
                Initialize from the 'main.py' with
                the maze's text file.
        """

        self.maze = maze
        self.hero = Hero()
        self.guard = Guard()
        self.items = Items()

        self.running = False

        # Initialize Pygamem module
        pygame.init()
        pygame.display.set_caption("Mac Guyver: The ecsape")


        # Set the dimension with the maze size tuple
        self.screen = pygame.display.set_mode(cfg.SCREEN)
        self.bg = pygame.Surface(cfg.SURFACE)

        for coord in self.maze.path:
            paths = pygame.image.load(cfg.PATH)
            self.bg.blit(
                paths, (
                    coord[0] * cfg.SPRITE,
                    coord[1] * cfg.SPRITE))

        for coord in self.maze.wall:
            walls = pygame.image.load(cfg.WALL)
            self.bg.blit(
                walls, (
                    coord[0] * cfg.SPRITE,
                    coord[1] * cfg.SPRITE))

    def game(self):
        self.running = True
        while self.running:
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.hero.img, self.hero.rect)
            self.screen.blit(self.guard.img, self.guard.rect)
            
            for key, images in zip(maze.item, (cfg.NEEDLE, cfg.SYRINGE, cfg.TUBE)):
                self.images = pygame.transform.scale(
                    pygame.image.load(images), cfg.ITEM_SIZE)

                self.all = self.images.get_rect()
                self.all.x = maze.item[key][0] * cfg.SPRITE
                self.all.y = maze.item[key][1] * cfg.SPRITE
                self.screen.blit(self.images, self.all)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    print("Quit the game")
            pygame.display.update()
#        else: 


        pygame.quit()
