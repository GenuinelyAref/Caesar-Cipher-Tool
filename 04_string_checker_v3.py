# string checker function

def str_checker(valid_chars):
    # take input
    text = input("Enter a text here: ")
    # change input text to lowercase
    text = text.lower()
    letter_chars_location = []
    # check that all characters are valid/permitted
    for i in range(0, len(text)):
        current_char = text[i]
        try:
            # attempt to find the character in the list of valid characters
            valid_chars.index(current_char)
            # if it's a letter, then add its index in the text to this list
            letter_chars_location.append(i)
        except ValueError:
            # if it's a non-letter character, ignore it
            pass
    # line break
    print("\n")
    # print all letters & their indexes from the given text (for testing purposes)
    for j in range(0, len(letter_chars_location)):
        current_index = letter_chars_location[j]
        print("There is a letter ({}), at index {} of the text given".format(text[current_index], current_index))
    # return list with the location of all letters in the given text
    return letter_chars_location


# lowercase english letters
lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                     "t", "u", "v", "w", "x", "y", "z"]
# uppercase english letters
uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                     "T", "U", "V", "W", "X", "Y", "Z"]

# All valid characters
all_chars = uppercase_letters + lowercase_letters

# Main routine
letter_indexes = str_checker(all_chars)
