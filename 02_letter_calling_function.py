# Letter calling function

# Letter calling function
def letter_call(letter_library, alphabet_order):
    # print correctly indexed letter
    return letter_library[alphabet_order-1]


# lowercase english letters
lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                     "t", "u", "v", "w", "x", "y", "z"]

# uppercase english letters
uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                     "T", "U", "V", "W", "X", "Y", "Z"]

# main routine
print("The 1st letter in the alphabet is \"{}\"".format(letter_call(lowercase_letters, 1)))
print("The 5th letter in the alphabet is \"{}\" (in uppercase)".format(letter_call(uppercase_letters, 5)))
print("The 26th letter in the alphabet is \"{}\" (in uppercase)".format(letter_call(uppercase_letters, 26)))
