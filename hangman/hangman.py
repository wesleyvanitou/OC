 # -*- coding: utf-8 -*-

import os
from pkg.tools import *
from pkg.functions import *

print(f"""
welcome to the hangman game!")
{hangmanpics[6]}\n
the goal is to find the word with
enough guessed letters. you have 7 chances
before losing. the remaining trial will be
your score.\n""".upper())

username = checker().capitalize() # Check if symbols in the username


# Clear the screen before starting the game
os.system('cls' if os.name == 'nt' else 'clear')



print(f"Hi {username}, Let's begin.")
