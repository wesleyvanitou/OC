# -*- coding: utf-8 -*- 

import os
from .tools import hangmanpics, words, symbols
import pickle


def checker(random, L="", i=0):
    """ The function will test if the letters are in the word"""
    W = "_" * len(random) # Mask the random word selected
    while random != W and i < len(hangmanpics):
        print("HANGMAN GAME")
        print(hangmanpics[i]) # Start with a blank hangman
        print(W.upper(), "\n")
        letter = input("ENTER LETTER HERE: ")
        L += letter # Create a string of already used letter
        hide = list("_" * len(random))
        if letter in random:
            for n, l in enumerate(random):
                if l in L:
                    hide[n] = random[n] # Replace masked letter with the right one
                    W = "".join(hide)
                    if W == random:
                        points = len(hangmanpics) - i
                        return W, points
        if letter not in random:
            L = L[:-1] # Remove the wrong letter from the string
            i += 1
            if i == len(hangmanpics):
                points = len(hangmanpics) - i
                return W, points
        os.system('cls' if os.name == 'nt' else 'clear')
