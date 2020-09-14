import random

from rock_paper_scissors import introduction #Makes it possible to run the functions in the other games
from hangman import hangman_game
from bagels_game import bagels_game
from lottery import Lottery_Game

GAMES = 4 #How many games you have


def intro():
    print("Hello, what would you like to play?") #Let's you choose what game you want to play, or quit
    print()
    print("Rock paper scissors:     1")
    print("Hangman:                 2")
    print("Bagels:                  3")
    print("Lottery:                 4")
    print("Suprise me:              S") #Chooses a game by random
    print("Quit:                    Q")
    
    what_game = input("> ").upper()

    if what_game == "1":
        print("Starting Rock paper scissors")
        introduction()
    elif what_game == "2":
        print("Starting Hangman")
        hangman_game()
    elif what_game == "3":
        print("Starting Bagels")
        bagels_game()
    elif what_game == "4":
        print("Starting Lottery")
        Lottery_Game()
    elif what_game == "S":
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
    elif what_game == "Q":
        print("Thank you for playing")
        quit()
    else:
        print("I didn't get that, please try again")
        intro()
    

while True: #Makes it possible so that you can end a function in the other games and then start the main again, ends when you want it to end
    intro()

#CREDITS
#Ella Rejström