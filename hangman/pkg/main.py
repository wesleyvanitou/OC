# -*- coding: utf-8 -*-
import os
from random import choice
from pkg import checker, tools, users, score

def main(username, score):
    random = choice(tools.words)
    W = "_" * len(random)

    trials = len(tools.hangmanpics)

    hangman = True

    while hangman:
        os.system('cls' if os.name == 'nt' else 'clear')
        W, points = checker.checker(random)
        if W == random:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""\nyou win. the word is '{random}'.
your score is {points} point(s) """.upper())
            hangman = False

            points += score[username]
            score[username] = points
            print()
            users.register(score, username, points)
        else:
            print(f"\nyou loose. the word was '{random}'".upper())
            C = input("Do you want to continue? (y or n): ".upper())
            C = C.lower()
            if C == 'y': continue
            else: 
                print("see you soon!".upper())
                hangman = False
