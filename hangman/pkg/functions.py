# -*- coding: utf-8 -*-

from .tools import symbols
# Check if the nickname is valid
def checker():
    """ The program will check if there aren't any special
characters in the name of the users."""
    while True:
        y = ""
        username = input("enter your username then press enter:\n".upper())
        for x in symbols:
            if x in username:
                y += x + ','
                continue
        if y:
            print(f"Symbols {y} are not allowed".isupper())
        else: 
            return username
#def match(letter, word):
#   """The function will take the word, mask it then analyze if
#the user find the right letter then display them."""

#    word = list(word)
#    mask = list('_' * len(word))

#    i = 0
#    while i < len(W):
#        if W[i] == letter:
#            mask[i] = word[i]
#        i += 1
#    return(''.join(mask))
