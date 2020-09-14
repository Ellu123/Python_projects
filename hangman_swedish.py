import random #Same as the english version but in swedish
from Words import computer_words_swedish


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
        print("DU HAR ANVÄNT UPP ALLA GISSNINGAR!")
        print()
        print("Ordet var:", word)
        play_again()

def word(): #Asks if you want to write an own word or if the computer shall randomize a word from a word list
    print()
    print("Vill du skriva ditt eget ord?")
    question = input("> ").upper()
    print()
    if question == "JA" or question == "J" or question == "JO" or question == "YES" or question == "Y":
        print("Vad är ditt ord?") 
        word = input("> ").upper()
        print()
        if "-" in word or " " in word or len(word) < 4: #Checks if your word is valid
            print("Du har inte valt ett giltigt ord, försök igen")
            word()
        else:
            print("Ordet är giltit")
            return word
    elif question == "NEJ" or question == "N" or question == "NO":
        word = random.choice(computer_words_swedish()).upper()
        while len(word) < 4:                                #Checks if the word is smaller than 4, if True --> Take another word
            word = random.choice(computer_words_swedish()).upper()
        print("Datorn har valt ett ord")
        return word
    else: 
        print("Jag förstod inte ditt svar, försök igen")
        print()
        word()

    
    


def hangman_game_swedish(): #Where the game is
    guesses = 0
    myWord = word()
    myWord_list = list(myWord)
    myWord_num = len(myWord)
    blanks = "_" * len(myWord)
    blanks_list = list(blanks)
    new_blanks_list = list(blanks)
    guess_list = []

    print("Låt oss spela hänga gubbe!")
    hangman_painting(guesses, myWord)
    print()
    print(" ".join(blanks_list ))
    print()
    print("Gissa ordet") 
    while guesses < 9: #Checks that you have guesses left
        print()
        guess = input("> ")
        guess = guess.upper()

        if len(guess) > 1 and len(guess) < myWord_num or len(guess) > myWord_num: #Checks that you are not cheating
            print("Svara med bara en bokstav!")
        if guess == "":
            print("Skriv något tack")
        elif guess in guess_list:
            print("Du har redan gissat den bokstaven")
            print("Det här är dom bokstäver som du har gissat redan\n", " ".join(guess_list)) #Prints out all the guesses letters if you guess the same letter
        else:
            guess_list.append(guess)
            i = 0
            
            while i < len(myWord): #Checks if your guess is in the word
                if guess == myWord_list[i]: 
                    new_blanks_list[i] = myWord_list[i]
                i += 1
            
            if guess == myWord:
                print("DU VANN!")
                print()
                print("\t .__.")
                print("\t(|  |)")
                print("\t (  )")
                print("\t _)(_")
                print()
                play_again()
                break

            if new_blanks_list == blanks_list:
                print("Din gissning finns inte i ordet")
                guesses += 1
                hangman_painting(guesses, myWord)

                if guesses < 9:
                    print("Gissa på nytt")
                    print(" ".join(blanks_list))
            
            elif myWord_list != blanks_list:

                blanks_list = new_blanks_list[:]
                print(" ".join(blanks_list))

                if myWord_list == blanks_list: #Checks if you have guessed the whole word
                    print("DU VANN!")
                    print()
                    print("\t .__.")
                    print("\t(|  |)")
                    print("\t (  )")
                    print("\t _)(_")
                    print()
                    play_again()
                    break
                else:
                    print("Bra gissning!")

def play_again(): #Asks if you want to play again, if no --> back to minigamemain
    print()
    print("Vill du spela på nytt?")
    again = input("> ").upper()
    if again == "JA" or again == "J" or again == "JO" or again ==  "YES" or again == "Y":
        hangman_game_swedish()
    elif again =="NEJ" or again == "N" or again == "NO":
        print()
    else:
        print("Jag förstod inte, försök på nytt")
        play_again()

#CREDITS
#Ella Rejström


                
        
        
        

    

















