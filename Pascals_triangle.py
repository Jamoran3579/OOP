

def make_new_row(old_row, counter):
    if old_row == []:
        new_row = [1]
    elif old_row == [1]:
        new_row = [1, 1]
    else:
        i = 1
        new_row = [1]
        while i < counter:
            new_row = new_row + [(int(old_row[i]) + int(old_row[i-1]))]
            i = i + 1
        new_row = new_row + [1]
    return new_row


j = 0
current_row = []
choice = " "
print("Welcome to pascals triangle generator\n")
nums = "1234567890101121314151617181920"
master_list = []

while choice not in nums:
    choice = input("Enter the desired height of Pascal's triangle: ")
    if choice not in nums:
        print("Invalid input, please try again\n")

while j < int(choice):
    current_row = make_new_row(current_row, j)
    master_list = master_list + [current_row]
    j = j + 1
print("Printing whole list of lists:")
print(master_list)

j = 0
print("Printing list of lists, one list at a time:")
while j < int(choice):
    print(master_list[j])
    j = j + 1


print("\nNow printing in the form of a normal pascals triangle:\n")
j = 0
str1 = ""
while j < int(choice):
    k = 0
    current_row = master_list[j]
    str1 = ' '.join([str(k) for k in current_row])
    str1 = str1.center(100)
    print(str1)
    j = j + 1

