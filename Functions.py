

def display_menu():
    print("Welcome to the functions menu, please enter which function you would like to run")
    print("0. Close the menu")
    print("1. Convert mass to energy")
    print("2. Count the number of consonants and vowels in an sentence")
    print("3. Calculate a particular number from the Fibonacci sequence")
    print("4. Store the date and time on the system")
    menu_choice()


def menu_choice():
    choice = input("")

    if choice == "0":
        return

    elif choice == "1":
        mass_to_energy()
        display_menu()

    elif choice == "2":
        letter_count()
        display_menu()

    elif choice == "3":
        fibonacci()
        display_menu()

    elif choice == "4":
        date_time()
        display_menu()

    else:
        print("Invalid menu option, please enter a valid option")
        display_menu()


def mass_to_energy():
    c = 299792458
    mass = int(input("Please enter a mass You would like to convert to energy"))
    print("The energy equivalent of the mass " + str(mass) + "kg is " + str(mass * c * c) + " Joules")
    print("Returning to menu......\n\n")


def letter_count():
    sentence = input("Please enter a sentence")
    count_consonants = count_vowels = 0
    consonants = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
    vowels = "aeiouAEIOU"
    i = 0

    while i < len(sentence):
        if sentence[i] in consonants:
            count_consonants = count_consonants + 1
        elif sentence[i] in vowels:
            count_vowels = count_vowels + 1
        i = i + 1

    print("The total number of vowels is " + str(count_vowels) + " and the total number of consonants is " +
          str(count_consonants))
    print("Returning to menu......\n\n")


def fibonacci():
    i = 1
    choice = ""
    while choice != "a" and choice != "b":
        choice = input("Would you like to print\na) The first n numbers of the fibonacci sequence" +
                       "\nb) The nth element of the fibonacci sequence\n")
        if choice != "a" and choice != "b":
            print("Please enter a valid choice\n\n")
    previous_element = 1
    current_element = 1
    next_element = 2

    n = int(input("What would you like n to equal to?"))

    while i < n:
        if choice == "a":
            print(previous_element)
        previous_element = current_element
        current_element = next_element
        next_element = previous_element + current_element
        i = i + 1
    print(previous_element)
    print("Returning to menu......\n\n")


def date_time():
    i = 0
    datetime = "DD/MM/YYYY HR:MIN:SEC"
    numbers = "0123456789"
    while datetime[2] != "/" or datetime[5] != "/" or datetime[10] != " " or datetime[13] != ":" or datetime[16] != \
            ":" or len(datetime) > 19 or datetime[0] not in numbers or datetime[1] not in numbers or datetime[3] not \
            in numbers or datetime[4] not in numbers or datetime[6] not in numbers or datetime[7] not in numbers or \
            datetime[8] not in numbers or datetime[9] not in numbers or datetime[11] not in numbers or datetime[12] \
            not in numbers or datetime[14] not in numbers or datetime[15] not in numbers or datetime[17] not in \
            numbers or datetime[18] not in numbers:
        datetime = input("What is the current date and time? \n" +
                         "Please enter it in the format DD/MM/YYYY HR:MIN:SEC\n")
        if datetime[2] != "/" or datetime[5] != "/" or datetime[10] != " " or datetime[13] != ":" or datetime[16] != \
                ":" or len(datetime) > 19 or datetime[0] not in numbers or datetime[1] not in numbers or datetime[3] \
                not in numbers or datetime[4] not in numbers or datetime[6] not in numbers or datetime[7] not in \
                numbers or datetime[8] not in numbers or datetime[9] not in numbers or datetime[11] not in numbers or \
                datetime[12] not in numbers or datetime[14] not in numbers or datetime[15] not in numbers or \
                datetime[17] not in numbers or datetime[18] not in numbers:
            print("Invalid format, please try again\n\n\n")
    while datetime[i] != " ":
        print(datetime[i])
        i = i + 1

    print("\n")

    i = 11
    while i < len(datetime):
        print(datetime[i])
        i = i + 1
    print("\n" + datetime[0:2] + datetime[6:9] + "\n")

    if int(datetime[11:12]) < 12:
        print("The time is a.m")
    print("Returning to menu......\n\n")


def main():
    display_menu()


main()


