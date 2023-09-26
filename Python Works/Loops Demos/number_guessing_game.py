# Number Guessing Game

"""
Creating an Application to Guess a Number Between 1-100 with 'Higher' and 'Lower' Statements

    -To do this you can use random module to generate a random number between 1-100
    -Every question is 20 points. Score is out of 100.
    -Take a input from the user for number of guesses. Every question will be counted as a guess.
"""

import random
import time

number = random.randint(1, 100)
number_of_guesses = int(input("How many guesses do you want? "))
counter = 0

print("Welcome to the Number Guessing Game!")

time.sleep(1)

print("I am thinking of a number between 1 and 100.")

time.sleep(1)

print("Can you guess what it is?")

while number_of_guesses > 0:
    number_of_guesses -= 1
    counter += 1
    
    guess = int(input("Guess: "))

    if guess == number:
        print(f"You guessed it in {counter} guesses! The number was {number}")
        time.sleep(0.5)
        print(f"Your score is {100 - (20 * (counter-1))}")
        break
    elif guess < number:
        print("Higher")
    else:
        print("Lower")
    
    if number_of_guesses == 0:
        print(f"You ran out of guesses! The number was {number}")
        break


