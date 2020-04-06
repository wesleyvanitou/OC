 # -*- coding: utf-8 -*-

import os
from pkg import checker, tools, users, score
from pkg.main import main

print(f"""
welcome to the hangman game!")
{tools.hangmanpics[7]}\n
the goal is to find the word with
enough guessed letters. you have 7 chances
before losing. the remaining trial will be
your score.\n""".upper())

username = users.username().capitalize() # Check if symbols in the username
print("\n")


score = score.score(username)
print(f"your score is {score[username]}\n".upper())
input("press enter to start".upper())

os.system('cls' if os.name == 'nt' else 'clear')

main(username, score)
