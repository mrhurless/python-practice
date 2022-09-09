"""
Prompts the user for a level, n. 

If the user does not input a positive integer, the program should prompt again.

Randomly generates an integer between 1 and n, inclusive, using the random module.

Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
    If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
    If the guess is larger than that integer, the program should output Too large! and prompt the user again.
    If the guess is the same as that integer, the program should output Just right! and exit.
"""
import sys
from random import randint

guess = ''
level = 0

while level < 1:
    try:
        level = int(input("Level: ").strip())
    except:
        level = int(input("Level: ").strip())    

rand = randint(1,level)

while guess != rand:
    guess = input("Guess: ").strip()
    try:
        guess = int(guess)
    except:
        pass    

    if type(guess) != int:
        pass
    elif guess < rand:
        print("Too small!")           
    elif guess > rand:
        print("Too large!")

print("Just Right!")
sys.exit()
# except:
# sys.exit()