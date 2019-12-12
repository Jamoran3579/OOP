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

print("The total number of vowels is " + str(count_vowels) + " and the total number of consonants is " + str(count_consonants))
