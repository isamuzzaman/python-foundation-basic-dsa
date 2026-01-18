# Number Guessing Game
import random
secret=random.randint(1,10)
for i in range(3):
    guess=int(input("Enter a number :"))
    if guess==secret:
        print("You Win!")
        break
    else:
        print("Wrong guess,try again!")    