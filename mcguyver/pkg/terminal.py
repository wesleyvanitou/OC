# -*- coding: utf-8 -*-

import os
from pkg import maze, hero

class Terminal:

    def __init__(self, maze, hero):
        self.maze = maze
        self.hero = player

    def game(self, console):
        print(self.maze.items())
        input()
        onsleep = False
        while not onsleep: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print(console)
            print("location: ", self.hero.locate)
            print("items: ", self.hero.grab)
            self.hero.controller()
            self.hero.locate,\
            self.hero.grab,\
            self.hero.item = \
            self.hero.move()
            if self.hero.locate == self.maze.guard:
                if len(self.hero.grab) == 3:
                    print("Guardian on sleep. You win")
                    onsleep = True
                else:
                    print("Missing item(s). You loose")
                    onsleep = True
