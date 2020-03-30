# -*- coding: utf-8 -*-

#+++++++++IMPORT++++++++++

# Standard libraries
import os
# Third party
import pygame

# Local applications
from pkg.settings import config as cfg, maze
from pkg.sprites.hero import Hero, HeroSpr
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
        self.hero = Hero()
        # Initialize Pygamem module
        pygame.init()
        pygame.display.set_caption("Mac Guyver: The ecsape")

        # Maze's dimension
        # ----------------
        screen =\
        surface = ((maze.size[0] + 1) * cfg.SPR_X,
                   (maze.size[1] + 1) * cfg.SPR_Y)

        self.screen = pygame.display.set_mode(screen)

        # Maze background generator
        # -------------------------
        self.bg = pygame.Surface(surface)

        for coord in maze.path:
            paths = pygame.image.load(cfg.PATH)
            self.bg.blit(
                paths, (
                    coord[0] * cfg.SPR_X,
                    coord[1] * cfg.SPR_Y))

        for coord in maze.wall:
            walls = pygame.image.load(cfg.WALL)
            self.bg.blit(
                walls, (
                    coord[0] * cfg.SPR_X,
                    coord[1] * cfg.SPR_Y))

            self.sprites = pygame.sprite.Group()
            self.sprites.add(hero)

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
            herospr = HeroSpr(maze.hero)
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(herospr.img, herospr.rect)
            self.screen.blit(self.guard.img, self.guard.rect)

            # Items generator
            # ---------------
            for key, images in zip(
                maze.item, (cfg.NEEDLE, cfg.SYRINGE, cfg.TUBE)):

                self.images = pygame.transform.scale(
                    pygame.image.load(images), cfg.SPR)
                self.all = self.images.get_rect()
                self.all.x = key[0] * cfg.SPR_X
                self.all.y = key[1] * cfg.SPR_Y
                self.screen.blit(self.images, self.all)

            # Core
            # ----
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    print("Quit the game")
                elif event.type == pygame.KEYDOWN:
                    maze.hero = self.hero.move(
                        self.hero.controller(event.key, maze.hero))
                    print(maze.hero, self.hero.stuck)
                    print(maze.item)
                    print("Grab", self.hero.grab)
                    if maze.hero == maze.guard:
                        if len(self.hero.grab) == cfg.NB_ITEMS:
                            running = False
                            print("You win!")
                        else:
                            running = False
                            print("You loose!")

#            self.sprites.update()
#            self.sprites.draw(self.screen)

            pygame.display.update()
        pygame.quit()
