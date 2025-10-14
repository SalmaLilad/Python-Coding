#VOLWEL COUNTER

def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0

    for char in string:
        if char in vowels:
            count += 1

    return count

string = input("Enter word: ")
vowel_count = count_vowels(string)
print(f"The number of vowels in your 'word' is: {vowel_count}")
