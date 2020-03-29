# -*- coding: utf-8 -*-

#+++++++++IMPORT++++++++++

# Standard libraries
import os
# Third party
import pygame

# Local applications
from pkg.settings import config as cfg
from pkg.settings  import maze
#from .settings.maze import Maze
from pkg.sprites.hero import Hero, Behavior
from pkg.sprites.guard import Guard

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
        self.guard = Guard()
        self.behavior = Behavior()
        self.hero = Hero()

        # Initialize Pygamem module
        pygame.init()
        pygame.display.set_caption("Mac Guyver: The ecsape")

        # Maze's dimension
        # ----------------
        screen =\
        surface = ((maze.size[0] + 1) * cfg.SPRITE,
                   (maze.size[1] + 1) * cfg.SPRITE)

        self.screen = pygame.display.set_mode(screen)

        # Maze background generator
        # -------------------------
        self.bg = pygame.Surface(surface)
        for coord in maze.path:
            paths = pygame.image.load(cfg.PATH)
            self.bg.blit(
                paths, (
                    coord[0] * cfg.SPRITE,
                    coord[1] * cfg.SPRITE))

        for coord in maze.wall:
            walls = pygame.image.load(cfg.WALL)
            self.bg.blit(
                walls, (
                    coord[0] * cfg.SPRITE,
                    coord[1] * cfg.SPRITE))

#            self.sprites = pygame.sprite.Group()
#            self.sprites.add(Hero(self.behavior.locate))

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
                    self.behavior.locate = \
                    self.hero.grab = self.behavior.move(
                        self.behavior.controller(event.key))
                    print(self.behavior.locate)
                    print(maze.item)
                    print("Grab", self.behavior.grab)
                    if self.behavior.locate == maze.guard:
                        if len(self.behavior.grab) == cfg.NB_ITEMS:
                            running = False
                            print("You win!")
                        else:
                            running = False
                            print("You loose!")

#            self.sprites.update()
#            self.sprites.draw(self.screen)

            pygame.display.update()
        pygame.quit()
