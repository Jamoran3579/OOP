print("We are going to create some simple rules for translating normal English into Gibberish\n"
      "Type two syllables and a word for it to be translated\n"
      "For every vowel, it will be replaced by a new syllable.\n"
      "If there are two vowels in a row, it will only apply to the second vowel.\n"
      "To request a vowel to be entered, use the '*' symbol, a vowel can only be put in front of a constant.\n"
      "When asked, type two syllables.\n"
      "Then type the word you wish to add them too.\n"
      "Your syllables should only contains letters or '*'.\n"
      "Enjoy the game!")
replay = 1
vowels = "aeiouAEIOU"
while replay == 1:
    Array2 = ""
    Gib1 = input("Please enter your first Gibberish syllable\n")
    Gib2 = input("Please enter your second Gibberish syllable\n")
    i = 0
    num = 0
    Array1 = input("Please enter a file you want to be translated\n")
    DoneWithFirstVowel = 0
    while Gib1[0].isdigit():
        print("Error, input must be a string, no integers")
        Gib1 = input("Please re-enter the first Gibberish syllable with no integers\n")

    while Gib2[0].isdigit():
        print("Error, input must be a string, no integers")
        Gib2 = input("Please re-enter the second Gibberish syllable with no integers\n")

    while i < len(Array1):
        if Array1[i] is ' ':
            DoneWithFirstVowel = 0
            Array2 = Array2 + Array1[i]
        elif Array1[i] in vowels:
            if DoneWithFirstVowel == 0:
                if Gib1[0] == '*':
                    Array2 = Array2 + Array1[i]
                    Array2 = Array2 + Gib1[1]
                    Array2 = Array2 + Array1[i]
                    DoneWithFirstVowel = 1
                else:
                    Array2 = Array2 + Gib1
                    Array2 = Array2 + Array1[i]
                    DoneWithFirstVowel = 1
            else:
                previous_character = Array1[i-1]
                if Gib2[0] == '*':
                    if previous_character not in vowels:
                        Array2 = Array2 + Array1[i]
                        Array2 = Array2 + Gib2[1]
                        Array2 = Array2 + Array1[i]
                    else:
                        previous_character = ""
                        Array2 = Array2 + Array1[i]
                else:
                    if previous_character not in vowels:
                        Array2 = Array2 + Gib2
                        Array2 = Array2 + Array1[i]
                    else:
                        previous_character = ""
                        Array2 = Array2 + Array1[i]
        else:
            Array2 = Array2 + Array1[i]
        i = i + 1
    print(Array2)
    AskReplay = input("Do you want to play again (yes or no)\n")
    if AskReplay == 'no' or AskReplay == 'n':
        replay = 0
        print("Thank you for playing")
    elif AskReplay == 'yes' or AskReplay == 'y':
        replay = 1