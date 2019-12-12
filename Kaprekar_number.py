

def print_kaprekar_nums(start, end):
    print("The list of all Kaprekar numbers from " + str(start) + " to " + str(end) + "is:")
    for i in range(start, end + 1):
        # Get the digits from the square in a list:
        sqr = i ** 2
        digits = str(sqr)

        # Now loop from 1 to length of the number - 1, sum both sides and check
        length = len(digits)
        for x in range(1, length):
            left = int("".join(digits[:x]))
            right = int("".join(digits[x:]))
            if (left + right) == i:
                print(str(i))


upper_limit = int(input("Enter a top limit (Inclusive): "))
print_kaprekar_nums(10, upper_limit)
