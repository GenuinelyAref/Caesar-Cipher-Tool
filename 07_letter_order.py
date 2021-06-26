# Find letter order in alphabet

def letter_order(letter, var_letter_library):
    return var_letter_library.index(letter.lower())+1


# Lists
# english letters
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                     "t", "u", "v", "w", "x", "y", "z"]

# Main routine
print("The order of the letter {} in the alphabet is: {}".format("A", letter_order("A", letters)))
print("The order of the letter {} in the alphabet is: {}".format("n", letter_order("n", letters)))
print("The order of the letter {} in the alphabet is: {}".format("z", letter_order("z", letters)))
