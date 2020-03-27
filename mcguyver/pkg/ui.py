# -*- coding: utf-8 -*-

#+++++++++IMPORT++++++++++

# Standard libraries

# Third party
import os, pygame

# Local applications
from pkg import maze, config as cfg
from pkg.hero import Behavior, Hero
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

            maze: class
                Initialize 'Maze' from the __init__  file
                with the 'labyrinth.txt'.
            hero: class
                Initialize the characteristics of the hero
            guard: class
                Initialize the characteristics of the Guardian
            screen: obj
                Generate the game's window
            bg: pygame obj
                Generate the surface where all the elements
                will be display
            # maze generator: loop
                Generator paths and walls
        """

        # Initialize the classes for internal use
        # ---------------------------------------
        self.maze = maze
        self.guard = Guard()
        self.behavior = Behavior()
        self.hero = Hero()

        # Initialize Pygamem module
        pygame.init()
        pygame.display.set_caption("Mac Guyver: The ecsape")


        # Maze's dimension
        # ----------------
        self.screen = pygame.display.set_mode(cfg.SCREEN)

        # Maze background generator
        # -------------------------
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

#            self.sprites = pygame.sprite.Group()
#            self.sprites.add(self.hero)

    def game(self):
        """
           GAME
           ----
           This is where the game will be displayed.

               Items generator
               ---------------
               The items will be generated trhough a zip loop
               with each value of the maze.item keys and a
               random list of items.

               Core
               ----
               The for loop goes trhough the the event.key
               inside the hero's' controller to test the
               direction and output the result.
        """

        # GAME
        # ----
        running = True
        while running:
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.hero.img, self.hero.rect)
            self.screen.blit(self.guard.img, self.guard.rect)

            # Items generator
            # ---------------
            for key, images in zip(
                maze.item, (cfg.NEEDLE, cfg.SYRINGE, cfg.TUBE)):

                self.images = pygame.transform.scale(
                    pygame.image.load(images), cfg.ITEM_SIZE)
                self.all = self.images.get_rect()
                self.all.x = key[0] * cfg.SPRITE
                self.all.y = key[1] * cfg.SPRITE
                self.screen.blit(self.images, self.all)

            # Core
            # ----
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    print("Quit the game")
                elif event.type == pygame.KEYDOWN:
                    self.behavior.locate = self.behavior.move(
                        self.behavior.controller(event.key))
                    print(self.behavior.locate)
                    print(maze.item)
            pygame.display.update()
        pygame.quit()
