import random


def Game():
    number = random.randint(1, 11)
    print("I have chooses a number between 1 and 10. Can you guess what it is?")
    guess = int(input("> "))

    while True:
        if guess == number:
            print("You've guessed the number")
            break
        elif guess < number:
            print("Higher")
            print()
            print("Guess again")
            guess = int(input("> "))
        elif guess > number:
            print("Lower")
            print()
            print("Guess again")
            guess = int(input("> "))
    play_again()


def play_again():  # Asks if you want to play again, if no --> go back to minigamemain
    print("Would you like to play again?")
    play_again = input("> ").upper()
    if play_again == "YES" or play_again == "Y":
        print()
        print()
        Game()
    elif play_again == "NO" or play_again == "N":
        print()
    else:
        print("I didn't understand, answer again")
        play_again()


Game()
