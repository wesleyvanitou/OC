# -*- coding: utf-8 -*-

from maze import Maze

maze = Maze()

class Hero(Maze):
    """Hero's behavior's within the maze"""

    def __init__(self):
        """Initialize the attribute"""
        self.locate = maze.player
        self.maze = maze
        self.grab = {}



    def controller(self, joystick):
        """This class creates the controller
        for the player base on the VIM Editor
        navigation system:
        h (Left), j (down),k (Up), l (Right)"""
        x, y = self.locate
        if joystick in "hH":
            joystick = (x, y - 1)
        elif joystick in "jJ":
            joystick = (x + 1, y)
        elif joystick in "kK":
            joystick = (x - 1, y)
        elif joystick in "lL":
            joystick = (x, y + 1)
        return joystick

    def move(self, joystick):
        """This method will allows the player to move."""
        if joystick in maze.paths:
            self.locate = joystick
        for key, value in maze.items.items():
            if value in joystick:
                self.grab[key] = value
                del maze.items[key]

        return self.locate, self.grab, maze.items

