# -*- coding: utf-8 -*-

from pkg import maze

class Hero:
    """Constructor"""

    def __init__(self, maze):
        """Constructor"""
        self.locate = \
        self.initial = maze.player
        self.maze = maze
        self.grab = []

    def controller(self):
        """This class creates the controller
        for the player base on the VIM Editor
        navigation system:
        h(←), j(↓), k(↑), l(→)"""
        x, y = self.locate
        self.initial = (x, y)
        # Depending of the playe's input, the coordinates will change
        joystick = input("\nMove McGuyver \nh(←), j(↓), k(↑), l(→): ")
        if joystick in "": # if no input, the player don't move
            joystick = (x, y)
        elif joystick in "hH": # Go Left
            joystick = (x, y - 1)
        elif joystick in "jJ": #Go Down
            joystick = (x + 1, y)
        elif joystick in "kK": #Go Up
            joystick = (x - 1, y)
        elif joystick in "lL": #Go Right
            joystick = (x, y + 1)
        return joystick

    def move(self, joystick):
        """This method will allows the player to move."""
        if joystick in self.maze.path:
            self.locate = joystick
            if self.locate in self.maze.item:
                self.grab.append(self.maze.item.pop(joystick))
        elif joystick in self.maze.wall: #If wall then initial coordinates
            self.locate = self.initial

        return self.locate, self.grab, self.maze.item
