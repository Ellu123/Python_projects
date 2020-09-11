import random

from rock_paper_scissors2 import introduction
from hangman import hangman_game
from bagels_game import bagels_game
from lottery import Lottery_Game

GAMES = 4


def intro():
    print("Hello, what would you like to play?")
    print()
    print("Rock paper scissors:     1")
    print("Hangman:                 2")
    print("Bagels:                  3")
    print("Lottery:                 4")
    print("Suprise me:              5")
    print("Quit:                    6")
    
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
        print("Starting Lottery")
        Lottery_Game()
    elif what_game == 5:
        rgame = random.randint(1, GAMES)
        if rgame == 1:
            print("Starting Rock paper scissors")
            introduction()
        elif rgame == 2:
            print("Starting Hangman")
            hangman_game()
        elif rgame == 3:
            print("Starting Bagels")
            bagels_game()
        elif rgame == 4:
            print("Starting Lottery")
            Lottery_Game()
    elif what_game == 6:
        print("Thank you for playing")
        quit()
    else:
        print("I didn't get that, please try again")
        intro()
    

while True:
    intro()