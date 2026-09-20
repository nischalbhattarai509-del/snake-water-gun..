# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun.
# The gun beats the snake, the water beats the gun, and the snake beats the water.
# Write a python program to create a Snake Water Gun game in Python using if-else statements.
import random

print(f"Welcome everyone to my snake water and gun game")

def check(comp, user):
    if comp == user:
        return 0
    if(comp == 0 and user ==1):
        return -1
    if(comp == 1 and user ==2):
        return -1
    if(comp == 2 and user ==2):
        return -1
        return 1


comp = random.randint(0,2)
user = int(input("Please Choose a number, 0 for snake, 1 for water and 2 for gun\n"))

score = check(comp, user)
print("You: ", user)
print("Computer: ", comp)

if (score == 0):
    print("Its a draw")
elif(score == -1):
    print("You have lost")
else:
    print("you won!!")