import os
from pkg import main, maze, player

filename = "pkg/labyrinth.txt"

maze = maze.Maze()
maze.path,\
maze.wall,\
maze.player,\
maze.guard = maze.load(filename)

player = player.Hero(maze)

game = main.Game(maze, player)
console = game.console(filename)
game.play(console)
