# Letter calling function - version 3

# Letter calling function
def letter_call(letter_library, alphabet_order, case):
    # find letter in english alphabet
    letter = letter_library[(alphabet_order-1) % 26]
    if case == "uppercase":
        # uppercase letter
        return letter.upper()
    elif case == "lowercase":
        # lowercase letter
        return letter


# english letters
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                     "t", "u", "v", "w", "x", "y", "z"]

# main routine
print("The {}th letter in the alphabet is \"{}\"".format(27, letter_call(letters, 27, "lowercase")))
print("The {}th letter in the alphabet is \"{}\" (in uppercase)".format(0, letter_call(letters, 0, "uppercase")))
print("The {}th letter in the alphabet is \"{}\"".format(-5, letter_call(letters, -5, "lowercase")))
print("The {}th letter in the alphabet is \"{}\" (in uppercase)".format(74, letter_call(letters, 74, "uppercase")))
