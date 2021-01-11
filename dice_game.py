import random

DICEMAX = 5  # The max ammount of dices you can get


def printDice(diceList, diceAmmount):  # Prints out the dices next to each other
    dices = {
        1: ["+-------------+", "|             |", "|             |", "|      0      |", "|             |", "|             |", "+-------------+"],
        2: ["+-------------+", "|  0          |", "|             |", "|             |", "|             |", "|           0 |", "+-------------+"],
        3: ["+-------------+", "|  0          |", "|             |", "|      0      |", "|             |", "|           0 |", "+-------------+"],
        4: ["+-------------+", "|  0        0 |", "|             |", "|             |", "|             |", "|  0        0 |", "+-------------+"],
        5: ["+-------------+", "|  0        0 |", "|             |", "|      0      |", "|             |", "|  0        0 |", "+-------------+"],
        6: ["+-------------+", "|  0        0 |", "|             |", "|  0        0 |", "|             |", "|  0        0 |", "+-------------+"]
    }

    if diceAmmount > 1:
        for i in range(7):
            for j in range(diceAmmount):
                if j < (diceAmmount - 1):
                    print(dices[diceList[j]][i], end=" ")
                else:
                    print(dices[diceList[j]][i])
    else:
        for i in range(7):
            for j in range(diceAmmount):
                if j < (diceAmmount - 1):
                    print(dices[diceList[-1]][i], end=" ")
                else:
                    print(dices[diceList[-1]][i])


def RollDice(diceAmmount, diceList):  # Rolls the dice
    i = 1
    print("Roll dice")
    input("> (Press Enter)")
    while i <= diceAmmount:
        diceNum = random.randint(1, 6)
        diceList.append(diceNum)
        i += 1
        print()
    print("You rolled: ")
    return diceList


def RollExtra(diceList):  # Rolls an extra dice
    diceNum = random.randint(1, 6)
    diceList.append(diceNum)
    print("You rolled:")
    return diceList


def Game():  # Where the full game is
    highScore = 0
    diceAmmount = 2
    points = 0
    keepGoing = True
    while keepGoing == True:
        diceList = []
        diceAdd = 0
        diceList = RollDice(diceAmmount, diceList)
        printDice(diceList, diceAmmount)
        currDiceAmmount = diceAmmount

        while True:  # Checks if you rolled a doubble
            j = 0
            x = 1
            for j in range(len(diceList)):
                equal = diceList.count(diceList[j])

                if equal >= 2 and diceAmmount < DICEMAX:
                    result = True
                    break
                else:
                    result = False
            if result == True:
                print("You rolled a double!")
                print()
                print("Roll an extra dice")
                ("> (Press Enter)")
                diceAmmount = 1
                diceList = RollExtra(diceList)
                printDice(diceList, diceAmmount)
                diceAmmount = currDiceAmmount + 1
                break
            else:
                break

        for i in range(len(diceList)):  # Adds all the dices together and counts how much it is
            diceAdd = diceAdd + diceList[i]
        diceSum = diceAdd

        if diceSum >= highScore:  # Checks if you have thrown higher lower or the same as your last throw
            highScore = diceSum
            points = points + highScore
            keepGoing = True
            print("Your current highscore:", highScore)

        else:
            print("Sorry but you lost :(")
            print("Total points:", points)
            print()
            keepGoing = False
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


def Introduction_dice():
    print()
    print("Hello and welcome to Roll the Dice!")
    print()
    print("The point in this game is to roll the dices and either getting higher or the same as the last roll")
    print("If the dices matches with eachother then you will get an extra dice")
    print()
    print("LET'S GO!!!")
    print()
    Game()

# CREDITS
# Ella Rejström
