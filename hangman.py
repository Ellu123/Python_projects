from hangman_swedish import hangman_game_swedish
from hangman_english import hangman_game_english

def Introduction_hm():
    print()
    print("In what language would you like to play or quit the game?")
    print("English --------- E")
    print("Swedish --------- S")
    print("Quit ------------ Q")
    choise = input("> ").upper()

    if choise == "E" or choise == "ENG" or choise == "ENGLISH":
        hangman_game_english()
    elif choise == "S" or choise == "SWE" or choise == "SWEDISH":
        hangman_game_swedish()
    elif choise == "Q" or choise == "QUIT":
        print()
    else:
        print("I didn't understand that, try again")


#Introduction_hm()