listA = [10, 20, 30, 40, 50, 0]
i = 0
listB = [0, 0, 0, 0, 0 ]
while i < 5:
    listB[i] = listA[i] + listA[i-1] + listA[i+1]
    i = i + 1
print(listB)
