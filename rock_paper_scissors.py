import random

def player(): #Player chooses what they want to play
    choice_list = [1, 2, 3]
    print("What would you like to play? ")
    print("Rock:\t\t1\nPaper:\t\t2\nScissors:\t3\n")
    while True:
        try:
            player_choice = int(input("> ")) #Loop so that you can't break the code if you write a letter
        except ValueError:
            print("Not an option")
            continue
        else:
            break
    while player_choice not in choice_list: #Check if your input is a valid answer
        print("Not an option")
        while True:
            try:
                player_choice = int(input("> "))
            except ValueError:
                print("Not an option")
                continue
            else:
                break

    return player_choice


def computer(): #Computer chooses by random what they want to play
    computer_hand = random.randint(1, 3)#1 = Rock, 2 = Paper, 3 = Scissors
    return computer_hand

def count(): #Player chooses how many rounds you will need to win the total game
    print("How many points will you need to win?")
    while True:
        try:
            point_count= int(input("> "))
        except ValueError:
            print("Not an option, try again")
            continue
        else:
            break
    return point_count


def game(): #Where the full game is
    player_count = 0
    computer_count = 0
    count_number = count()
    while computer_count < count_number and player_count < count_number:
        player_hand = player()
        computer_hand = computer()
         
        hand_def = { #hand_def = hand defenition
            1: "Rock",
            2: "Paper",
            3: "Scissors"
        }

        if player_hand == computer_hand: #All the possible ways of how the game will turn out and what the code shall do
            print("You chose", hand_def[player_hand], "and the computer chose", hand_def[computer_hand], ". It's a tie")
        elif player_hand == 1 and computer_hand == 2:
            print("You chose", hand_def[player_hand], "and the computer chose", hand_def[computer_hand], ". Computer won the round")
            computer_count += 1
        elif player_hand == 2 and computer_hand == 3:
            print("You chose", hand_def[player_hand], "and the computer chose", hand_def[computer_hand], ". Computer won the round")
            computer_count += 1
        elif player_hand == 3 and computer_hand == 1:
            print("You chose", hand_def[player_hand], "and the computer chose", hand_def[computer_hand], ". Computer won the round")
            computer_count += 1
        else:
            print("You chose", hand_def[player_hand], "and the computer chose", hand_def[computer_hand], ". You won the round")
            player_count += 1
        print(player_count, computer_count)
        print()
    
    if player_count > computer_count: #If player has won
        print("You won!")
        print()
        print("\t .__.\n\t(|  |)\n\t (  )\n\t _)(_")#prints out a trophy
        print("    (Grodan Greger)")
        print()
        play_again()
    elif computer_count > player_count: #If computer won
        print("Computer won!")
        print()
        play_again()

def play_again(): #Asks if you want to play again, if no --> go back to minigamemain
    print("Would you like to play again?")
    play_again = input("> ").upper()
    if play_again == "YES" or play_again == "Y":
        print()
        print()
        game()
    elif play_again == "NO" or play_again == "N":
        print()
    else:
        print("I didn't understand, answer again")
        play_again()



def Introduction_rps():
    print()
    print("Hello and welcome to rock paper scissors!")
    print("The rules are simple. Rock takes scissors, paper takes rock, scissors take paper and vice versa")
    print()
    game()



#CREDITS
#Ella Rejström
#Ana Bensabat

    