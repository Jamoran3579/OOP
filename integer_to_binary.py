integer = input("Please enter an integer")
integer = int(integer)
i = 0

print("\nInteger : ", integer)

str1 = ""
binary_count = -1

while integer > 0:
    if integer % 2 == 1:
        str1 = str1+"1"
    else:
        str1 = str1+"0"
    binary_count = binary_count + 1
    if integer == 1 or integer == 0:
        break
    integer = integer // 2

print(str1)
str2 = ""

while binary_count > -1:
    str2 = str2 + str1[binary_count]
    binary_count = binary_count - 1
    i = i + 1

print("Binary = ", str2)
