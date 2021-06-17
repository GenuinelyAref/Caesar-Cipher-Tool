# Letter calling function - version 2

# Letter calling function
def letter_call(letter_library, alphabet_order):
    # call letter from the alphabet in order
    num = alphabet_order % 26
    return letter_library[num-1]


# lowercase english letters
lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                     "t", "u", "v", "w", "x", "y", "z"]

# uppercase english letters
uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                     "T", "U", "V", "W", "X", "Y", "Z"]

# main routine
print("The {}th letter in the alphabet is \"{}\"".format(27, letter_call(lowercase_letters, 27)))
print("The {}th letter in the alphabet is \"{}\" (in uppercase)".format(0, letter_call(uppercase_letters, 0)))
print("The {}th letter in the alphabet is \"{}\"".format(-5, letter_call(lowercase_letters, -5)))
print("The {}th letter in the alphabet is \"{}\" (in uppercase)".format(74, letter_call(uppercase_letters, 74)))
