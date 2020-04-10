print("WELCOME TO MAD LIBS!!!")
import time 

playagain = "y"

while playagain == "Y" or playagain == "y" or playagain == "yes":
    noun = input ("Enter a noun...")
    p_noun = input("Enter a plural noun...")
    noun2 = input("Enter a noun...")
    place = input ("Enter a noun...")
    adj = input("Enter a adjective...")
    noun3 = input ("Enter a noun...")

    print("------------------------------------")
    print("Be kind to your "+noun+"-footed "+p_noun)
    print ("For a duck may be somebody's", noun2,",")
    print ("Be kind to your",p_noun,"in",place)
    print ("Where the weather is always",adj,".")
    print ()
    print ("You may think that is this the",noun3,",")
    print ("Well it is.")
    print ("------------------------------------------")
    
    playagain = input ("Do you wanna play again??y/n")

