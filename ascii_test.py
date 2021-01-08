import random

# dices = {
#     1: ["+-------------+", "|             |", "|             |", "|      0      |", "|             |", "|             |", "+-------------+"],
#     2: ["+-------------+", "|  0          |", "|             |", "|             |", "|             |", "|           0 |", "+-------------+"],
#     3: ["+-------------+", "|  0          |", "|             |", "|      0      |", "|             |", "|           0 |", "+-------------+"],
#     4: ["+-------------+", "|  0        0 |", "|             |", "|             |", "|             |", "|  0        0 |", "+-------------+"],
#     5: ["+-------------+", "|  0        0 |", "|             |", "|      0      |", "|             |", "|  0        0 |", "+-------------+"],
#     6: ["+-------------+", "|  0        0 |", "|             |", "|  0        0 |", "|             |", "|  0        0 |", "+-------------+"]
# }

# # k = 1
# # for i in range(len(dices[1])):
# #     print(dices[k][i], end=" ")
# #     print(dices[k][i])

# # for i in range(7):
# #     for j in range(6):
# #         k = j + 1
# #         if j <= 4:
# #             print(dices[k][i], end=" ")
# #         else:
# #             print(dices[k][i])

# diceList = [3]
# diceAmmount = 1
# for i in range(7):
#     for j in range(diceAmmount):
#         if j < (diceAmmount - 1):
#             print(dices[diceList[j]][i], end=" ")
#         else:
#             print(dices[diceList[j]][i])

# # TODO: Make it possible to make two different dices next to each other
# # * DONE ^
# # TODO: Turn it to the dice game
# # * DONE ^

diceList = [6, 4, 5, 3, 5]

for i in range(len(diceList)):
    equal = diceList.count(diceList[i])

    if equal >= 2:
        print("DET FINNS PAR!!")
        break
    else:
        print("INGA PAR HÄR!!")

# x = diceList.count(6)

# print(x)
