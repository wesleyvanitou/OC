# -*- coding: utf-8 -*-

import os
from random import choice
from pkg import checker, tools, users, score

def main(username, score):

    trials = len(tools.hangmanpics)

    hangman = True

    while hangman:
        random = choice(tools.words)  # Choose a random word from the function  
        os.system('cls' if os.name == 'nt' else 'clear') # Refresh the screen each time
        W, points = checker.checker(random)
        if W == random:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""\nyou win. the word is '{random}'.
our score is {points} point(s) """.upper())
            hangman = False

            points += score[username]
            score[username] = points
            print()
            users.register(score, username, points)
        else:
            print(f"\nyou loose. the word was '{random}'".upper())
            points += score[username]
            score[username] = points
            print()
            users.register(score, username, points)

            C = input("\nDo you want to continue? (y or n): ".upper())
            C = C.lower()
            if C == 'y': continue
            else: 
                print("see you soon!".upper())
                hangman = False
