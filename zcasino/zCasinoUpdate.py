#-*-coding:utf-8-*

import os, random, math

#Assign the number the user choose to numUser and convert it with int
user_nbr = int(input("Hi, Choose a number between 0 and 49: "))

table_nbr = random.randrange(50) # Pick a random number on the roulette

# Assign the amount of money the user have.
user_money = int(input("Put your money on the table \n"))

# Assign the amount of money the user will bet.
bet = int(input("How much do you want to bet? \n"))

# Verify if the number is in range


print ("The table's number is {0} and yours is {1}".format(tableNum, userNum))
print ("You've bet {} EUR".format(bet))

if user_number == table_number: # if the number matches, the user wins.
    print("Congratulations! You win", str(bet * 3), "EUR")

if user_nbr != table_nbr and user_nbr % 2 == table_nbr % 2:
    if numUser % 2 == 0: # The remainder is 0 so it is an even number.
        print("""
              You loose but at least you have the same 'Black' color.
              You can keep half of your bet which is """ 
              , str(math.ceil(bet / 2)), " EUR.\n")
    else:
        print("""
              You loose but at least you have the same 'red' color.
              You can keep half of your bet which is """ 
              , str(math.ceil(bet / 2)), " EUR.\n")
else:
    print("Sorry, You lose.") # If nothing matches, the user loose.

# Pause for windows user
os.system("pause")
