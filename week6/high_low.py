# Example by James Fairbairn <j.fairbairn@tees.ac.uk>
# We wrote this together in class.
#
# **DO NOT REMOVE THIS HEADER**
#
# Notes:
#   + This file is for demonstration purposes only.
#   + You must use this example to guide your own solution.
#     **DO NOT SUBMIT THIS FILE AS IS FOR ASSESSMENT**

import random

MAX_GUESSES = 5
RANGE_START = 1
RANGE_END = 30

number = random.randint(RANGE_START,RANGE_END)

name = input("Hello! What is your name? ")
print(name, ", I am thinking of a number between ", RANGE_START, " and ", RANGE_END, ".", sep="")

guesses_taken = 0
while guesses_taken < MAX_GUESSES:
    guess = int(input("Please enter a number: "))
    guesses_taken += 1

    if guess < number:
        print("Your guess is too low!")
    elif guess > number:
        print("Your guess is too high!")
    else:
        break
# end while loop

if guess == number:
    print("Awesome, ", name, "! You guessed correctly in ", guesses_taken, " attempts!", sep="")
else:
    print("Nope. The number I was thinking of was", number)
