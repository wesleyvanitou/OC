import random, math


game = True

while game:
    i = input("Enter the number between 0 and 49: ")
    while i not in range(50):
        print("y")
        break
    else:
        print("n")
