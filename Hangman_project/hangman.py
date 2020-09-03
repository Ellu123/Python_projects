import random

def hangman_painting(guesses, word):
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

def word():
    print()
    question = input("Do you wanna write a own word? ").upper()
    print()
    if question == "YES" or question == "Y":
        word = input("What is your word?: ").upper()
        print()
        if "-" in word or " " in word:
            print("You have not chosen a valid word, try again")
            word()
        else:
            print("Valid word")
            return word
    elif question == "NO" or question == "N":
        word = random.choice(computer_words()).upper()
        return word
    else: 
        print("I didn't understand the answer, please try again")
        print()
        word()

    
    


def game():
    guesses = 0
    myWord = word()
    myWord_list = list(myWord)
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
    while guesses < 9:
        print()
        guess = input("> ")
        guess = guess.upper()

        if len(guess) > 1:
            print("Only one letter please!")
        elif guess == "":
            print("Fill in something please")
        elif guess in guess_list:
            print("You have already guessed that")
            print("These are the ones you have guessed this far\n", " ".join(guess_list))
        else:
            guess_list.append(guess)
            i = 0
            
            while i < len(myWord):
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

                if myWord_list == blanks_list:
                    print("YOU WON!")
                    print()
                    print("\t .__.")
                    print("\t(|  |)")
                    print("\t (  )")
                    print("\t _)(_")
                    print()
                    play_again()
                else:
                    print("Great Guess! Guess another")

def play_again():
    print()
    again = input("Would you like to play again? ").upper()
    if again == "YES" or again == "Y":
        game()
    elif again =="NO" or again == "N":
        print("Bye for now")
        quit()
    else:
        print("I didn't understand your answer, please try again")
        play_again()


                
        
        
        

    

def computer_words():
    word_choises = ["Hello", "Love", "Jazz"]
    return word_choises



game()











