import random

# Makes it possible to run the functions in the other games
from rock_paper_scissors import Introduction_rps
from hangman import Introduction_hm
from bagels_game import bagels_game
from lottery import Lottery_Game

GAMES = 4  # How many games you have


def Intro():
    # Let's you choose what game you want to play, or quit
    print("Hello, what would you like to play?")
    print()
    print("Rock paper scissors: --- 1")
    print("Hangman: --------------- 2")
    print("Bagels: ---------------- 3")
    print("Lottery: --------------- 4")
    print("Suprise me: ------------ S")  # Chooses a game by random
    print("Quit: ------------------ Q")

    what_game = input("> ").upper()

    print("Created by: Ella Rejström")

    if what_game == "1":
        print("Starting Rock paper scissors")
        Introduction_rps()
    elif what_game == "2":
        print("Starting Hangman")
        Introduction_hm()
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
            Introduction_rps()
        elif rgame == 2:
            print("Starting Hangman")
            Introduction_hm()
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
        Intro()


while True:  # Makes it possible so that you can end a function in the other games and then start the main again, ends when you want it to end
    Intro()

# CREDITS
# Ella Rejström
