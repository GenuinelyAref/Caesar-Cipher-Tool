# Caesar Cipher function

# Libraries


# FUNCTIONS
# letter calling function
def letter_call(letter_library, alphabet_order, case):
    # find letter in english alphabet
    letter = letter_library[(alphabet_order-1) % 26]
    if case == "uppercase":
        # uppercase letter
        return letter.upper()
    elif case == "lowercase":
        # lowercase letter
        return letter


# blank checking function
def not_blank(prompt, error_message):
    # take input
    user_input = input(prompt)
    # check if input is blank / only spaces
    while user_input.strip(" ") == "":
        # print error message
        print("{}\n".format(error_message))
        # retake input
        user_input = input(prompt)
    return user_input


# string checker function
def str_checker(valid_chars):
    # take input
    text = input("Enter a text here: ")
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


# Lists/variables
# english letters
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                     "t", "u", "v", "w", "x", "y", "z"]

# Main routine
# Main routine
letter_indexes = str_checker(letters)
print(letter_indexes)
