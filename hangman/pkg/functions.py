# -*- coding: utf-8 -*- from .tools import * import pickle # Check if the nickname is valid 

import os
from .tools import symbols
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

def scoreboard(username):
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

def checker(random, L=""):
    W = "_" * len(random)
    print(random)
    while random != W:
        print(W.upper())
        letter = input("Enter letter: ")
        L += letter
        hide = list("_" * len(random))
        for i, y in enumerate(random):
            if y in L:
                hide[i] = random[i]
                W = "".join(hide)
        os.system('cls' if os.name == 'nt' else 'clear')
