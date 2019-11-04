# -*- coding: utf-8 -*- 

import os
from .tools import hangmanpics, words, symbols
import pickle


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
                        points = len(hangmanpics) - i
                        return W, points
        if letter not in random:
            L = L[:-1]
            i += 1
            if i == len(hangmanpics):
                points = 0
                return W, points
        os.system('cls' if os.name == 'nt' else 'clear')
