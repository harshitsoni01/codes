print("GUESS THE NUMBER!!!!")
import random
import time 

randnum = random.randint(1,1000)
guess = -2
guesstaken = 0

while guesstaken <= 10:
    guess = input("Take a guess!!\n")
    guess = int(guess)
    guesstaken+=1 

    if guess < randnum:
        print("Your guess is low!!")
    elif guess > randnum:
        print("YOur guess is high!!") 
    elif guess == randnum:
        break 
    

if guess == randnum:
    print("YAYY!! YOu guessed the correct number")
    guesstaken = str(guesstaken)
    time.sleep(0.5)
    print("You took "+guesstaken+" tries")    
elif guess != randnum:
    randnum = str(randnum)
    print("Sorry. You loss. The number was "+randnum)    
