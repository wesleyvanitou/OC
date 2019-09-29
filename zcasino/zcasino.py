import random


numUser = int(input("Hi, Choose a number between 0 and 49: "))
#bet = int(input("How much do you want to bet? "))
numTable = int(random.randint(0,49))

print ("The table's number is {0} and yours is {1}".format(numTable, numUser))

if numUser == numTable: 
    print("Congratulations! You win" + str(bet * 3)  + "EUR")
elif numUser != numTable and numUser % 2 == numTable % 2:
        print("Same color.")
else:
    print("Lose.")

