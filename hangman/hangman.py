 # -*- coding: utf-8 -*-

import os
from pkg.tools import *
from pkg.functions import *
from random import choice

print(f"""
welcome to the hangman game!")
{hangmanpics[6]}\n
the goal is to find the word with
enough guessed letters. you have 7 chances
before losing. the remaining trial will be
your score.\n""".upper())

username = username().capitalize() # Check if symbols in the username
print("\n")


score = scoreboard(username)
print(f"your score is {score[username]}\n")
input("press enter to start".upper())

os.system('cls' if os.name == 'nt' else 'clear')

random = choice(words)

checker(random)

