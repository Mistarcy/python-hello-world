from random import randint

play_again = "yes"
while play_again == "yes":
    x = input("Please enter a number x: ")
    y = input("Please enter a number y: ")
    x = int(x)
    y = int(y)
    enters = input("Please enter a number 1-4: ")
    if enters == "1":
        print(x+y)
    elif enters == "2":
        print(x-y)
    elif enters == "3":
        print(x*y)
    elif enters == "4":
        print(x/y)
    else:
        break
    play_again = input("Want to play again?")
