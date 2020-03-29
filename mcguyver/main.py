# -*- coding: utf-8 -*-

#+++++++++IMPORT++++++++++

# Standard libraries
import os

# Thrid party
# Put third party tools here!

# Local applications
from  pkg.ui import Display
#from pkg.hero import Hero, Behavior

#+++++++++++++++++++++++++


# Initialize classes
display = Display()

def macguyver():
    """Initialize the game"""
    display.game()

if __name__ == "__main__":
    macguyver()
