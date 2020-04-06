import os
from random import randrange
from math import ceil

game = True


print("""Welcome.
Please have a seat.\n""")

while game:
    money = 0
    while money == 0:
        money = input("How much money did you bring: ")
        try:
            money = int(money)
        except ValueError:
            print("This is not a  number.")
            money = 0
            continue 
        if money == 0:
            print("It's not a free game. Let's be serious")
        else:
            print("Welcome, you've bring", money, "EUR")

    number = -1
    while number not in range(50):
        number = input("Enter the number (Between 0 - 49) you want to bet on: ")
        try:
            number = int(number)
        except ValueError:
            print("This is not a number")
            number = -1
            continue
        if number not in range(50):
            print("The number is out of range: ")

    bet = 0
    while bet not in range(1, money):
        bet = input("How much do you want to bet? ")
        try:
            bet = int(bet)
        except ValueError:
            print("This is not a number")
            bet = 0
            continue
        if bet not in range(1, money):
            print("You cannot bet 0 or below what you have.")
game = False
