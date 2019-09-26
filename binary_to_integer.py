binary_num = input("Please enter a binary number")

i = 0
integer = 0
power = len(binary_num) - 1

while i < len(binary_num)-1:
    if binary_num[i] == "1":
        integer = integer + 2**power
    i = i + 1
    power = power - 1

print(integer)
