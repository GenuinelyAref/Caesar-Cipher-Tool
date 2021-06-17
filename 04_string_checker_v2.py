# string checker function

def str_checker(valid_chars):
    condition = False
    # repeat until valid input is given
    while not condition:
        # take input
        text = input("Enter a text here: ")
        # change input text to lowercase
        text = text.lower()
        # check that all characters are valid/permitted
        for i in range(0, len(text)):
            try:
                # attempt to find the character in the list of valid characters
                valid_chars.index(text[i])
                # then character would be valid
                condition = True
            except ValueError:
                # if character is not found in the valid characters list, then the string is not valid
                condition = False
                # print error message
                print("\033[3mSorry this is an invalid input - please letters and punctuation only\033[0m\n")
                break
    # when all characters are valid then the whole string is valid
    print("\033[3mValid input\033[0m\n")


# lowercase english letters
lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                     "t", "u", "v", "w", "x", "y", "z"]
# uppercase english letters
uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                     "T", "U", "V", "W", "X", "Y", "Z"]
# special characters
special_chars = [",", " ", ".", "\"", "\'", "?", "!", "(", ")", ":", ";", "-", "_", "/", "\\"]
# All valid characters
all_chars = lowercase_letters + uppercase_letters + special_chars


# Main routine
str_checker(all_chars)
