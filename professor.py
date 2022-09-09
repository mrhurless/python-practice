"""
Prompts the user for a level, n. 

If the user does not input 1, 2, or 3, the program should prompt again.

Randomly generates ten (10) math problems formatted as X + Y = , wherein 
each of X and Y is a non-negative integer with n digits. 

No need to support operations other than addition (+).

Prompts the user to solve each of those problem. If an answer is not correct 
(or not even a number), the program should output EEE and prompt the user again, 
allowing the user up to three tries in total. 

If the user has still not answered correctly after three tries, the program 
should output the correct answer.

The program should ultimately output the user’s score, a number out of 10.

Structure your program as follows, wherein get_level prompts (and, if need be, 
re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer 
returns a randomly generated non-negative integer with level digits or raises 
a ValueError if level is not 1, 2, or 3:
"""

import random

levels = [1,2,3]

def main():
    score = 0
    level = get_level()

    for i in range (0,10):
        x = generate_integer(level)
        y = generate_integer(level)
        solution = x + y
        answer = ""

        #while type(answer) not int:
        for n in range(0,3):
            try:
                answer = int(input(str(x) + " + " + str(y) + " = "))
                if answer == solution:
                    score += 1
                    break
                else:
                    print("EEE")
            except:
                print("EEE")

        if answer != solution:
            print(str(x) + " + " + str(y) + " = " + str(solution))
    
    print("Score: " + str(score))

def get_level():
    level = ''
    while level not in levels:
        try:
            level = int(input("Level: ").strip())
        except:
            pass
            #level = int(input("Level: ").strip())   

    return level   

def generate_integer(level):
    result = 0

    if level == 1:
        result = random.randint(0,9)
    elif level == 2:
        result = random.randint(10,99)
    elif level == 3:
        result = random.randint(100,999)
    
    return result

if __name__ == "__main__":
    main()