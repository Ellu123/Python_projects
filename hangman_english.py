import random
from Words import computer_words_english


def hangman_painting(guesses, word): #Prints out the hangman and checks if you have lost
    if guesses == 0:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print("________")
        print("|      |")
    elif guesses == 1:
        print()
        print("")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("________")
        print("|      |")
    elif guesses == 2:
        print()
        print("________")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("________")
        print("|      |")
    elif guesses == 3:
        print()
        print("________")
        print("|     |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("________")
        print("|      |")
    elif guesses == 4:
        print()
        print("________")
        print("|     |")
        print("|     O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("________")
        print("|      |")
    elif guesses == 5:
        print()
        print("________")
        print("|     |")
        print("|     O")
        print("|     |")
        print("|     |")
        print("|")
        print("|")
        print("________")
        print("|      |")
    elif guesses == 6:
        print()
        print("________")
        print("|     |")
        print("|     O")
        print("|    \\|")
        print("|     |")
        print("|")
        print("|")
        print("________")
        print("|      |")
    elif guesses == 7:
        print()
        print("________")
        print("|     |")
        print("|     O")
        print("|    \\|/")
        print("|     |")
        print("|")
        print("|")
        print("________")
        print("|      |")
    elif guesses == 8:
        print()
        print("________")
        print("|     |")
        print("|     O")
        print("|    \\|/")
        print("|     |")
        print("|    /")
        print("|")
        print("________")
        print("|      |")
    elif guesses == 9:
        print()
        print("________")
        print("|     |")
        print("|     O")
        print("|    \\|/")
        print("|     |")
        print("|    / \\")
        print("|")
        print("________")
        print("|      |")
        print()
        print("YOU LOSE!")
        print()
        print("The word was:", word)
        play_again()

def word(): #Asks if you want to write an own word or if the computer shall randomize a word from a word list
    print()
    print("Do you wanna write a own word?")
    question = input("> ").upper()
    print()
    if question == "YES" or question == "Y":
        print("What is your word?") 
        word = input("> ").upper()
        print()
        if "-" in word or " " in word or len(word) < 4: #Checks if your word is valid
            print("You have not chosen a valid word, try again")
            word()
        else:
            print("Valid word")
            return word
    elif question == "NO" or question == "N":
        word = random.choice(computer_words_english()).upper()
        while len(word) < 4:                                #Checks if the word is smaller than 4, if True --> Take another word
            word = random.choice(computer_words_english()).upper()
        print("The computer has chosen a word")
        return word
    else: 
        print("I didn't understand the answer, please try again")
        print()
        word()

    
    


def hangman_game_english(): #Where the game is
    guesses = 0
    myWord = word()
    myWord_list = list(myWord)
    myWord_num = len(myWord)
    blanks = "_" * len(myWord)
    blanks_list = list(blanks)
    new_blanks_list = list(blanks)
    guess_list = []

    print("Let's play hangman!")
    hangman_painting(guesses, myWord)
    print()
    print(" ".join(blanks_list ))
    print()
    print("Guess the word") 
    while guesses < 9: #Checks that you have guesses left
        print()
        guess = input("> ")
        guess = guess.upper()

        if len(guess) > 1 or len(guess) < myWord_num or len(guess) > myWord_num: #Checks that you are not cheating
            print("Only one letter please!")
        elif guess == "":
            print("Fill in something please")
        elif guess in guess_list:
            print("You have already guessed that")
            print("These are the ones you have guessed this far\n", " ".join(guess_list)) #Prints out all the guesses letters if you guess the same letter
        else:
            guess_list.append(guess)
            i = 0
            
            while i < len(myWord): #Checks if your guess is in the word
                if guess == myWord_list[i]: 
                    new_blanks_list[i] = myWord_list[i]
                i += 1
            
            if new_blanks_list == blanks_list:
                print("Your letter isn't here")
                guesses += 1
                hangman_painting(guesses, myWord)

                if guesses < 9:
                    print("Guess again")
                    print(" ".join(blanks_list))
            
            elif myWord_list != blanks_list:

                blanks_list = new_blanks_list[:]
                print(" ".join(blanks_list))

                if myWord_list == blanks_list: #Checks if you have guessed the whole word
                    print("YOU WON!")
                    print()
                    print("\t .__.")
                    print("\t(|  |)")
                    print("\t (  )")
                    print("\t _)(_")
                    print()
                    play_again()
                    break
                else:
                    print("Great Guess! Guess another")

def play_again(): #Asks if you want to play again, if no --> back to minigamemain
    print()
    print("Would you like to play again?")
    again = input("> ").upper()
    if again == "YES" or again == "Y":
        print()
    elif again =="NO" or again == "N":
        print()
    else:
        print("I didn't understand your answer, please try again")
        play_again()

#CREDITS
#Ella Rejström


                
        
        
        

    

















