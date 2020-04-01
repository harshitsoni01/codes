import random
import time
import sys
min = 1
max = 6

def dicee():
    roll_again = "yes"
    diceq = input("\nDo you want one or two dice??1/2 ")    
    if diceq == "1":
        while roll_again == "yes" or roll_again == "y" or roll_again == "Y":
            print("Rolling dice...")
            time.sleep(0.3)
            print("The value is... ")
            time.sleep(0.5)
            print(random.randint(min,max))
            roll_again = input("Roll the dice again??y/n")
    elif diceq == "2":
        while roll_again == "yes" or roll_again == "y" or roll_again == "Y":
            print("Rolling dices...")
            time.sleep(0.3)
            print("The values are... ")
            time.sleep(0.5)
            print(random.randint(min,max))
            print(random.randint(min,max))
            roll_again = input("Roll the dice again??y/n")
    else:
        print("I did not understand that. Try again by pressing return")

while 1:
    print("\n\tWELCOME TO DICE SIMULATOR!!")
    print("\n\tWHERE YOU GET RANDOM NUMBERS FROM 1-6!!")
    dicee()
    sys.exit()