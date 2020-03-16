# -*- coding: utf-8 -*-

import os
from pkg import maze, player

class Game:

    def __init__(self, maze, player):
        self.maze = maze
        self.player = player

    def console(self, filename):
        with open(filename) as console:
            console = console.read()
        return console


    def play(self, console):
        print(self.maze.items())
        input()
        onsleep = False
        while not onsleep: 
            os.system('cls' if os.name == 'nt' else 'clear')
            print(console)
            print("location: ", self.player.locate)
            print("items: ", self.player.grab)
            self.player.locate,\
            self.player.grab,\
            self.player.item = \
            self.player.move(self.player.controller())
            if self.player.locate == self.maze.guard:
                if len(self.player.grab) == 3:
                    print("Guardian on sleep. You win")
                    onsleep = True
                else:
                    print("Missing item(s). You loose")
                    onsleep = True
