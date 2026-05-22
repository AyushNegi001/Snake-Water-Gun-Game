"""
snake  water gun game 

"""


import random 
'''
1 for snake
-1 for water
0 for gun 
 
'''

computer = random.choice([1,-1,0])
youstr = input("enter your choice : ")
youDict = {"snake": 1, "water": -1, "gun": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}
               
you = youDict[youstr]               

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")


if (computer == you):
    print("draw")

else:
    if(computer == -1 and you == 1):
        print("you win!")

    elif(computer == -1 and you == 0):
        print("you lose!")

    elif(computer == 1 and you == -1):
        print("you lose!")


    elif(computer == 1 and you == 0):
        print("you lose!")

    elif(computer == 0 and you == -1):
        print("you lose!")

    elif(computer == 0 and you == 1):
        print("you lose!")
 
    else:
        print("something went wrong")
