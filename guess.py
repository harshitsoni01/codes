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
    time.sleep(0.5)
    guesstaken = int(guesstaken)    
    if guesstaken == 1 or guesstaken == 2:
        print("You are a SUPERHUMAN!")
    elif guesstaken == 3 or guesstaken == 4:
        print("You are a genius.")
    elif guesstaken == 5 or guesstaken == 6:
        print("You are an expert.")
    elif guesstaken == 7 or guesstaken == 8:
        print("You are good.")
    elif guesstaken == 9 or guesstaken == 10 or guesstaken == 11:
        print("You can do better.")
        
elif guess != randnum:
    randnum = str(randnum)
    print("Sorry. You loss. The number was "+randnum)
