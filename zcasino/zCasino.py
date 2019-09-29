#-*-coding:utf-8-*

import os
import random
import math

#Assign the number the user choose to numUser and convert it with int
numUser = int(input("Hi, Choose a number between 0 and 49: "))

# Assign the amount of money the user will bet.
bet = int(input("How much do you want to bet? \n"))

numTable = random.randrange(50) # Pick a random number on the roulette

# Recap of the number, the result of the roulette and the bet
print ("The table's number is {0} and yours is {1}".format(numTable, numUser))
print ("You've bet {} EUR".format(bet))

if numUser == numTable: # if the number matches, the user wins.
    # Print the winning message
    print("Congratulations! You win", str(bet * 3), "EUR")

# if numbers didn't match but the remainders are the same:
if numUser != numTable and numUser % 2 == numTable % 2:
    if numUser % 2 == 0: # The remainder is 0 so it is an even number.
        # Print the message for black color
        print("""
              You loose but at least you have the same 'Black' color.
              You can keep half of your bet which is """ 
              , str(math.ceil(bet / 2)), " EUR.\n")
    #Otherwise it is red, so print the message
    else:
        print("""
              You loose but at least you have the same 'red' color.
              You can keep half of your bet which is """ 
              , str(math.ceil(bet / 2)), " EUR.\n")
else:
    print("Sorry, You lose.") # If nothing matches, the user loose.

# Pause for windows user
os.system("pause")
