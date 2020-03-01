# -*- coding: utf-8 -*-

import maze


class Hero:
    """Constructor"""

    def __init__(self, maze):
        """Constructor"""
        self.locate = maze.player
        self.maze = maze
        self.grab = []

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
        if joystick in maze.path:
            self.locate = joystick
        if joystick in maze.item:
            self.grab.append(maze.item.pop(joystick))

        return joystick, self.grab, maze.item

maze = maze.Maze()  
maze.load("labyrinth.txt")

hero = Hero(maze)
item = maze.items()
print(item)
print("player location ", hero.locate)
joystick = hero.controller("j")
print("move to ", joystick)

joystick, grab, item = hero.move(joystick)

print(joystick)
print(grab)
print(item)
