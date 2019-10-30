# -*- coding: utf-8 -*- from .tools import * import pickle # Check if the nickname is valid 

import os
from .tools import *
import pickle


def username():
    """ The program will check if there aren't any special
characters in the name of the users."""
    while True:
        y = ""
        username = input("enter your username then press enter: ".upper())
        for x in symbols:
            if x in username:
                y += x + ','
                continue
        if y:
            print(f"Symbols {y} are not allowed".upper())
        else: 
            return username

def register(score, username, user_score):
    print("SCORES")
    for value, key in score.items():

        print(f"{key} ", value)

    with open('scores', 'wb') as F:
        score[username] = user_score
        pickle.dump(score, F)

def score(username):
    """The function will check if the scoreboard exist, if not,
create a new one and add the user into it."""
    try:
        with open('scores', 'rb') as F:
            S = pickle.load(F)
            if username in list(S.keys()):
                print(f"Welcome back {username}".upper())
            else:
                S[username] = 0
                print(f"Welcome for your first time {username}".upper())
    except:
        with open('scores', 'wb') as F:
            S = {username: 0}
            pickle.dump(S, F)
            print(f"Empty file. Welcome {username}".upper())
    return S

def checker(random, L="", i=0):
    """ The function will test if the letters are in the word"""
    W = "_" * len(random)
    found = True
    while random != W and i < len(hangmanpics):
        print("HANGMAN GAME")
        print(hangmanpics[i])
        print(W.upper(), "\n")
        letter = input("ENTER LETTER HERE: ")
        L += letter
        hide = list("_" * len(random))
        if letter in random:
            for n, l in enumerate(random):
                if l in L:
                    hide[n] = random[n]
                    W = "".join(hide)
                    if W == random:
                        user_score = len(hangmanpics) - i
                        return W, user_score
        if letter not in random:
            L = L[:-1]
            i += 1
        os.system('cls' if os.name == 'nt' else 'clear')
