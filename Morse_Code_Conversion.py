#Converting sentences to Morse Code

MORSE_CODE_DICT = {
    'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ',':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'
}

def sentence_to_morse(sentence):
    sentence = sentence.upper()
    morse_sentence = [MORSE_CODE_DICT[char] for char in sentence] #the character you are taking in the sentence is from the dictionary MORSE_CODE_DICT
    return ' '.join(morse_sentence)



def flip_dict(dictionary):
    flipped_dictionary = {}
    for original_key, original_value in dictionary.items():
        flipped_dictionary[original_value] = original_key
    return flipped_dictionary

FLIPPED_MORSE_CODE_DICT = flip_dict(MORSE_CODE_DICT)


def morse_to_sentence(morse_sentence):
    morse_sentence
    return ''.join(FLIPPED_MORSE_CODE_DICT)

# Example usage
if __name__ == "__main__":
    sentence = "You will never understand this"
    print(sentence_to_morse(sentence))
