# Example by Saul Johnson <saul.johnson@tees.ac.uk>
# We wrote this together in class.
#
# **DO NOT REMOVE THIS HEADER**
#
# Notes:
#   + This file is for demonstration purposes only.
#   + You must use this example to guide your own solution.
#     **DO NOT SUBMIT THIS FILE FOR ASSESSMENT**

# Import the randint function from the random library.
from random import randint

# Loop, starting off with play_again equal to "yes" so we enter the loop for the first time.
play_again = "yes"
while play_again == "yes":
    num = input("Please enter a number between 1 and 6: ") # Get a numberfrom the user.
    num = int(num)

    # Generate a random number.
    rand_num = randint(1, 6)

    # Do the two numbers match?
    if num == rand_num:
        print("Congratulations!")
    else:
        print("Better luck next time!")

    # Ask the user if they would like to play again.
    play_again = input("Want to play again?")
