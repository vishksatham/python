"""
Learn about conditional statements (if, elif, else) for decision making.
Understand loops (for, while) for iterating over sequences or executing code repeatedly.
"""

import random

x = random.randint(1, 10)

counter = 0


while True:

    y = int(input("Guess a number between 1 and 10: "))
    counter += 1

    if y == x:

        print("You guessed the correct random number in " + counter + " attempts!")
        break

    else:
        print("Incorrect answer, guess again!")