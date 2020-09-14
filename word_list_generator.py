word_list = []
word = ""
print("Put in words and it will generate it to a list")
while word != "end":
    word = input("> ")
    word_list.append(word)

word_list.remove("end")
word_list = list(dict.fromkeys(word_list))

print(word_list)
