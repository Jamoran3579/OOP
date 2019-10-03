import random
i = 1
sentence = input("Please enter a word to be scrambled")
print(sentence)
position1 = 0
position2 = 0
new_sentence = ""
holder = 0
str2 = ""
j = 0
m = 0
k = 0
while i < 10:
    while sentence[m] != " ":
        m = m + 1
    str1 = sentence[k:m]
    m = m + 1
    k = m
    position1 = random.randrange(1, len(str1)-1)
    position2 = random.randrange(1, len(str1)-1)
    if position1 == position2:
        if position1 == len(str1):
            position1 = position1 - 1
        else:
            position1 = position1 + 1
    j = 0
    if position1 > position2:
        position1, position2 = position2, position1
    #print(position1, position2)
    while j < position1:
        str2 = str2 + str1[j]
        j = j + 1
        #print("1")
    #print(str2)
    str2 = str2 + str1[position2]
    j = position1 + 1
    #print("2")
    while j < position2:
        str2 = str2 + str1[j]
        j = j + 1
        #print("3")
    #print(str2)
    str2 = str2 + str1[position1]
    j = position2 + 1
    #print("4")
    while j < len(str1):
        str2 = str2 + str1[j]
        j = j + 1
        #print("5")
    print(str2)
    i = i + 1
    new_sentence = new_sentence + str2
    str2 = ""
    #print("6")

print(new_sentence)





















































































































































































































































































































































































































































































































