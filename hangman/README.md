The Hangman game!

The goal of this game is to discover the right word by findind the
right letters. You don't need to find all the letter to find the word.
So each time you try a letter the program will notiy you and replace the
start that ask it. You will have a limited amount of try.

The player has to give his name because it will be stored on a scoreboard.
The project will be stored in 3 files:

- The game (hangman.py)
  The game will ask the name of the user then display a blank hangman.
  As long as the player find the right letter the hangman will stay
  blank. The game has to display the number of trials left next to 
  the player name

  Player: Wesley
  Trial left: 06 out of 07

#  +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
T******ER

Enter a letter:


- The scoreboard (scores.py)
  When the user will finish the game the scoreboard will be printed.
  SCORES
  - 01 - Wesley - 12 words
  - 02 - Alpha - 08 words
  - 03 - Steeve - 01 words
  - 04 -
  - 05 -

- The game assets (assets.py)
  This file will have all the words, the trial left
- The game functions
  So what type of functions will be in the file?
  - The function that will encrypt the words
  - The function that will test if the letter input
    by the user is the right one.
