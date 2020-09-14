import random

LOTTO_NUM = 5 #How many numbers you can have, easier to change
MONEY = 100 #How much money you have, easier to change


def What_Do_Now(play_money): #Checks if you want to keep going, start over or end game
    print()
    print("What do you want to do now?")
    if play_money == 0:         #If you don't have any money left --> takes out the option of keep going
        print()
        print("Start all over:   S")
        print("End game:         E")
        do_now = input("> ").upper()

        if do_now == "S" or do_now == "E":
            return do_now        
        else:
            print("I didn't understand that, try again")
            What_Do_Now(play_money)
    else:
        print()
        print("Keep playing:     K")
        print("Start all over:   S")
        print("End game:         E")
        do_now = input("> ").upper()

        if do_now == "K" or do_now == "S" or do_now == "E":
            return do_now        
        else:
            print("I didn't understand that, try again")
            What_Do_Now(play_money)

def Player_Choise(): #Where you choose what will be your lucky numbers
    choise_list = []
    print("What will be your lucky numbers? Max %s numbers" %(LOTTO_NUM))
    for i in range (0, LOTTO_NUM):
        choise = input("> ")
        choise_list.append(choise)
        while len(choise_list[i]) > 2 or choise_list[i] == "" or choise_list[i].startswith("-") or choise_list[i].startswith("0"): #Checks if you have valid numbers
            print("Invalid number, try again!")
            del choise_list[i]
            choise = input("> ")
            choise_list.append(choise)
            if len(choise_list[i]) > 2 or choise_list[i] == "" or choise_list[i].startswith("-") or choise_list[i].startswith("0"):
                continue
            else:
                break

            
        print("Number", i + 1, "has been chosen")
        print(" ".join(choise_list))
    print()
    print("Your number sequense is valid")
    return choise_list
    
 

def Lottery_Num(): #Randomizes out the correct numbers
    number = []
    for i in range(0, LOTTO_NUM):
        number.append(random.randint(1, 99))
    return number
        


def Check_wins(lN, pN, bet, player_money): #Checks if you have won anything and add money to your "bank"
    right = 0
    totalright = 0
    wrong = 0
    for i in range(0, LOTTO_NUM):
        if int(pN[i]) == lN[i]:
            totalright += 1
        elif int(pN[i]) in lN:
            right += 1
        else:
            wrong += 1
    
    if wrong == LOTTO_NUM:
        print("None of your numbers matched the lotto numbers :(")
        player_money = player_money - bet
        return player_money
    else:
        print("You had %s of the same numbers but on the wrong place and %s of the same and on the right place" %(right, totalright))
        player_money = player_money + ((2 * totalright) * bet) + ((1 * right) * bet) #Counts how much money you get
        return player_money
    

def Money_Check(pM): #Checks that you have any money left and prints out how much money you have
    if pM > 0:
        if pM == 1:                         #Checks if you have 1 or more coins so that the grammar is correct
            print("You have %s coin" %(pM))
            return pM
        else:
            print("You have %s coins" %(pM))
            return pM
    else:
        print("You are out of money")
        return pM

        
def Money_Bet(player_money): #Asks how much money you want to bet
    print("How much money do you want to bet?")
    while True:             #Checks so that you can't bug the program and shut it down
        try:
            bet = int(input("> "))
        except ValueError:
            print("Not a valid number")
            continue
        else:
            break
    while bet == 0 or bet > player_money or bet == "" or bet < 0: #Checks that your bet is valid
        print("Not a valid bet")
        while True:
            try:
                bet = int(input("> "))
            except ValueError:
                print("Not a valid number")
                continue
            else:
                break
    print("Bet is valid!")
    return bet


    
def Player_Money(): #Return how much money you have to start with
    the_player_money = MONEY
    return the_player_money

    

def Lottery_Game(): #Where the whole game is 
    play_money = Player_Money()
    while True:
        play_money = Money_Check(play_money)
        bet = Money_Bet(play_money)
        lottery_numbers = Lottery_Num()
        player_numbers = Player_Choise()
        play_money = Check_wins(lottery_numbers, player_numbers, bet, play_money)
        print("The correct numbers were", lottery_numbers)
        play_money = Money_Check(play_money)
        do_now = What_Do_Now(play_money)
        if do_now == "K": #Checks what you what to do
            continue
        elif do_now == "S":
            Lottery_Game()
        else:
            print()
            break

#CREDITS
#Ella Rejström
        



    
