import random


#NUM_DIGITS = 3 #How long the number it is, this makes it easier to change
MAX_GUESS = 10 #How many guesses you have, this makes it easier to change
def difficulty():
    print("Choose your difficulty")
    print("Normal (3 digits, 10 guesses) -------- N")
    print("Hard (5 digits, 10 guesses) -----------H")
    dif = input("> ").upper()

    if dif == "N" or dif == "NORMAL":
        num_digits = 3
        #MAX_GUESS = 10
        return num_digits
    elif dif == "H" or dif == "HARD":
        num_digits = 5
        #MAX_GUESS = 10
        return num_digits#, MAX_GUESS
    else:
        print("I didn't understand that, try again")
        difficulty()
def playAgain(): #The play again function, if no --> back to minigamemain
    print()
    print("Would you like to play again?")
    playagain = input("> ").upper()

    if playagain == "YES" or playagain == "Y":
        bagels_game()
    elif playagain == "NO" or playagain == "N":
        print()
        
    else:
        print("I didn't understand it. Try again")
        playAgain()

def getSecretNum(num_digits): #Randomises the secret number
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    secretNum = ""
    for i in range(num_digits):
        secretNum += str(numbers[i])
        secretNum_list = list(secretNum)
    return secretNum


def getClues(guess, secretNum): #Checks if you have all right, some right or nothing right
    if guess == secretNum:
        print("You figured it out!")
        print()
        print("\t .__.")
        print("\t(|  |)")
        print("\t (  )")
        print("\t _)(_")
        print()
    
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagles"
    
    clues.sort()
    return " ".join(clues)

def isOnlyDigits(num): #Check if it is a valid guess
    if num == "":
        return False
    
    for i in num:
        if i not in "1 2 3 4 5 6 7 8 9".split():
            return False
        
        return True



def bagels_game(): #Where the full game is
    num_digits = difficulty()
    print()
    print("Hello")
    print("I am thinking of a %s-digit number. Can you figure out what it is?" %(num_digits))
    print("I will give you only three types of clues")
    print()
    print("When I say:\tThat means:")
    print("Bagels:\t\tNone of the digits is correct\nPico:\t\tOne digit is correct but in the wrong position\nFermi:\t\tOne digit is correct and in the right position")
    print()


    secretNum = getSecretNum(num_digits)
    print("Secret number has been chosen. You have %s guesses to get it" %(MAX_GUESS))
    guessesTaken = 1
    while guessesTaken <= MAX_GUESS: #Checks if you have any guesses left
        guess = ""
        while len(guess) != num_digits or not isOnlyDigits(guess):
            print("Guess #%s:" %(guessesTaken))
            guess = input("> ")
                    
        print(getClues(guess, secretNum))
        guessesTaken += 1

        if guess == secretNum:
            playAgain()
            break
        if guessesTaken > MAX_GUESS:
            print("You ran out of guesses. The correct answer was %s" %(secretNum))
            playAgain()
            break

#CREDITS
#Ella Rejström
     
     
            



 
