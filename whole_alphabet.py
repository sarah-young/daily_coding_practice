import string

def whole_alphabet(input_str):
    """Take in a string.
     Return 1 if all the letters in the alphabet are in the string.
     Return 0 otherwise."""

    alphabet_set = set(string.ascii_lowercase)
    check_set = set()

    for letter in input_str:
        letter = letter.lower()
        if letter.isalpha():
             check_set.add(letter)

    if alphabet_set == check_set:
        return 1
    else:
        return 0
