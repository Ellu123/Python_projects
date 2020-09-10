import random

from rock_paper_scissors2 import introduction
from hangman import hangman_game
from bagels_game import bagels_game


def intro():
    print()
    print("Hello, what would you like to play?")
    print()
    print("Rock paper scissors:     1")
    print("Hangman:                 2")
    print("Bagels:                  3")
    print("Suprise me:              4")
    print("Quit:                    5")
    
    what_game = int(input("> "))

    if what_game == 1:
        print("Starting Rock paper scissors")
        introduction()
    elif what_game == 2:
        print("Starting Hangman")
        hangman_game()
    elif what_game == 3:
        print("Starting Bagels")
        bagels_game()
    elif what_game == 4:
        rgame = random.randint(1, 3)
        if rgame == 1:
            print("Starting Rock paper scissors")
            introduction()
        elif rgame == 2:
            print("Starting Hangman")
            hangman_game()
        elif rgame == 3:
            print("Starting Bagels")
            bagels_game()
    elif what_game == 5:
        print("Thank you for playing")
        quit()
    else:
        print("I didn't get that, please try again")
        intro()

intro()