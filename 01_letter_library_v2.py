lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", 
                     "t", "u", "v", "w", "x", "y", "z"]
uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                     "T", "U", "V", "W", "X", "Y", "Z"]

indexes = [0, 25, 26]
for i in range(0,  3):
    try:
        index = uppercase_letters[indexes[i]]
    except IndexError:
        index = "Error - no letter at this index"
    print("Index value {}: {}".format(indexes[i], index))
