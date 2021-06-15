# lowercase english letters
lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                     "t", "u", "v", "w", "x", "y", "z"]

# uppercase english letters
uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                     "T", "U", "V", "W", "X", "Y", "Z"]

# testing indexes for documentation
indexes = [0, 25, 26]
for i in range(0,  3):
    # if index is in range
    try:
        index = uppercase_letters[indexes[i]]
    # if index is out of range
    except IndexError:
        index = "Error - no letter at this index"
    print("Index value {}: {}".format(indexes[i], index))
