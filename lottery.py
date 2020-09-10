import random

LOTTO_NUM = 5

def player_choise():
    choise_list = []
    print("What will be your lucky numbers? Max %s numbers" %(LOTTO_NUM))
    for i in range (0, LOTTO_NUM):
        choise = input("> ")
        choise_list.append(choise)
        while len(choise_list[i]) > 2 or choise_list[i] == "" or choise_list[i].startswith("-") or choise_list[i].startswith("0"):
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
    
 

def lottery_num():
    number = []
    i = 0
    while i <= LOTTO_NUM:
        number.append(random.randint(1, 9))
        i += 1
    return number
        


#def check_wins():

#def betting():

def lotter_game():
    lottery_numbers = lottery_num()
    player_numbers = player_choise()

player_choise()