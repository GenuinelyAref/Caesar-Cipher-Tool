# string checker function

def str_checker(valid_chars):
    condition = False
    while not condition:
        text = input("Enter a text here: ")
        text = text.lower()
        for i in range(0, len(text)):
            try:
                x = valid_chars[text[i]]
                condition = True
            except IndexError:
                condition = False
                break


# lowercase english letters
lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                     "t", "u", "v", "w", "x", "y", "z"]
# uppercase english letters
uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                     "T", "U", "V", "W", "X", "Y", "Z"]
# special characters
special_chars = [",", " ", ".", "\"", "\'", "?", "!", "(", ")", ":", ";", "-", "/"]
# All valid characters
all_chars = lowercase_letters + uppercase_letters + special_chars


# Main routine
str_checker(all_chars)
