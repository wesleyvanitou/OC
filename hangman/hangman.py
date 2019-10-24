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

username = checker().capitalize() # Check if symbols in the username
print("\n")


score = scoreboard(username)
print(f"your score is {score[username]}\n")
input("press enter to start".upper())

os.system('cls' if os.name == 'nt' else 'clear')

random = choice(words)
mask = list('_' * len(random))
word = list(random)

trials = len(hangmanpics)

while word != mask or trials != 0:
    i = 0 
    while i < len(random):
        print(hangmanpics[i])
        print(random)
        print(' '.join(mask).upper(), "\n")
        letter = input("enter the letter here: ".upper())
        if random[i] == letter:
            mask[i] = word[i]
            i += 1
        os.system('cls' if os.name == 'nt' else 'clear')
