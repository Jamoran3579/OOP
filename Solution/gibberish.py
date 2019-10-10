# Program that gets users word and put letter into the word to create a gibberish word
# 07/10/2019


print("Welcome to The Gibberish game.\nThe rules of the are as follows, you will be asked to enter a word.\n"
      "This word will then be converted into gibberish. You will then be asked to enter the first syllable for the first vowel in the word.\n"
      "After you must enter the second syllable for the rest of the vowels. If you enter an astrix, then the vowel will save and\n"
      "the astrix will be turned into the vowel. At the end of the game you have the choice of ending the game or playing again.\n\n")

file = input("Please enter a file you wish to translate: ")

my_file1 = open(file, "r")
my_file2 = open("inputFileGibberish.txt", "w")


#Function that creates gibberish word
def game():
    gibberish_word = ""
    vowels = "aeiouAEIOU"
    j = 0
    num = "1234567890"
    tester1 = 0
    tester2 = 0
    gib_word1 = ""
    gib_word2 = ""
    word = my_file1.read()

    while tester1 != 1:
        gib_word1 = input("Please enter the first syllable to be entered at the first vowel: ")

        if gib_word1[0] in num or gib_word1[1] in num:
            print("Please enter valid characters or wildcard(*)")
        else:
            tester1 = 1

    while tester2 != 1:
        gib_word2 = input("Please enter the second syllable to be entered at the rest of the vowels: ")

        if gib_word2[0] in num or gib_word2[1] in num:
            print("Please enter valid characters or wildcard(*)")
        else:
            tester2 = 1

    while word[j] not in vowels:
        gibberish_word = gibberish_word + word[j]
        j = j + 1

    if "*" in gib_word1:
        gib_word1 = word[j] + gib_word1[1:]
        gibberish_word = gibberish_word + gib_word1
        gibberish_word = gibberish_word + word[j]
    else:
        gibberish_word = gibberish_word + gib_word1
        gibberish_word = gibberish_word + word[j]
    j = j + 1

    while j < len(word):
        if word[j] not in vowels:
            gibberish_word = gibberish_word + word[j]
        elif word[j - 1] in vowels:
            gibberish_word = gibberish_word + word[j]
        elif "*" in gib_word2:
            gib_word2 = word[j] + gib_word2[1:]
            gibberish_word = gibberish_word + gib_word2
            gibberish_word = gibberish_word + word[j]
            gib_word2 = "*" + gib_word2[1:]
        else:
            gibberish_word = gibberish_word + gib_word2
            gibberish_word = gibberish_word + word[j]
        j = j + 1

    print("Your final sentence is: " + gibberish_word)
    my_file2.write(gibberish_word)
    print("Your results can be found in the file inputFileGibberish.txt")



#calling function
game()


#ask user if they want to play again
count = 0

while count == 0:
    play_again = input("Do you want to play again? (y/n)")
    if play_again == 'y' or play_again == 'Y' or play_again == 'yes' or play_again == 'Yes':
        game()
        count = 0
    elif play_again == 'n' or play_again == 'N' or play_again == 'no' or play_again == 'No':
        print("Thank you for playing!")
        count = 1

    else:
        print("Please enter a valid input")

my_file1.close()
