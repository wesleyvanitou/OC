 # -*- coding: utf-8 -*-

import os
from pkg.tools import *
from pkg.functions import *
from random import choice

print(f"""
welcome to the hangman game!")
{hangmanpics[7]}\n
the goal is to find the word with
enough guessed letters. you have 7 chances
before losing. the remaining trial will be
your score.\n""".upper())

username = username().capitalize() # Check if symbols in the username
print("\n")


score = score(username)
print(f"your score is {score[username]}\n".upper())
input("press enter to start".upper())

os.system('cls' if os.name == 'nt' else 'clear')

random = choice(words)
W = "_" * len(random)

trials = len(hangmanpics)

hangman = True

while hangman:
    W, user_score = checker(random)
    os.system('cls' if os.name == 'nt' else 'clear')
    if W:
        print(f"""you win. the word is '{W}.'
your score is {user_score} point(s) """.upper()) 
        hangman = False

        user_score += score[username]
        score[username] = user_score
        register(score, username, user_score)
    else:
        print("you loose. the word was {W}")
        hangman = False


