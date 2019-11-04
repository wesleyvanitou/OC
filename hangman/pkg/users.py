# -*- coding: utf-8 -*- 

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

def register(score, username, points):
    """ This hangman function will register the user's score when he wins"""
    print("SCORES")
    for value, key in score.items():
        print(f"{key} ", value)

    with open('scores', 'wb') as F:
        score[username] = points
        pickle.dump(score, F)

