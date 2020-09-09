import random


NUM_DIGITS = 3
MAX_GUESS = 10

def playAgain():
    print()
    print("Would you like to play again?")
    playagain = input("> ").upper()

    if playagain == "YES" or playagain == "Y":
        bagels_game()
    elif playagain == "NO" or playagain == "N":
        print("Bye for now")
    else:
        print("I didn't understand it. Try again")
        playAgain()

def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    secretNum_list = list(secretNum)
    while 0 in secretNum_list:
        secretNum = ""
        for i in range(NUM_DIGITS):
            secretNum += str(numbers[i])
        secretNum_list = list(secretNum)

    
    return secretNum

def getClues(guess, secretNum):
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

def isOnlyDigits(num):
    if num == "":
        return False
    
    for i in num:
        if i not in "1 2 3 4 5 6 7 8 9".split():
            return False
        
        return True



def bagels_game():
    print()
    print("Hello")
    print("I am thinking of a %s-digit number. Can you figure out what it is?" %(NUM_DIGITS))
    print("I will give you only three types of clues")
    print()
    print("When I say:\tThat means:")
    print("Bagels:\t\tNone of the digits is correct\nPico:\t\tOne digit is correct but in the wrong position\nFermi:\t\tOne digit is correct and in the right position")
    print()


    secretNum = getSecretNum()
    print("Secret number has been chosen. You have %s guesses to get it" %(MAX_GUESS))
    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ""
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
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
     
     
            



 
