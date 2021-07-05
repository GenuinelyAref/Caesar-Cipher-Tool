# Caesar Cipher function

# Libraries
import random


# FUNCTIONS
# random key-picking function
def random_key_pick():
    return random.randint(1, 25)


# letter calling function
def letter_call(var_letter_library, alphabet_order, case):
    # find letter in english alphabet
    letter = var_letter_library[(alphabet_order-1) % 26]
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
def str_checker(var_letter_library):
    # take input
    text = input("Enter a text here: ")
    var_text = text.lower()
    letter_chars_location = []
    # check that all characters are valid/permitted
    for i in range(0, len(var_text)):
        current_char = var_text[i]
        try:
            # attempt to find the character in the list of valid characters
            var_letter_library.index(current_char)
            # if it's a letter, then add its index in the text to this list
            letter_chars_location.append(i)
        except ValueError:
            # if it's a non-letter character, ignore it
            pass
    # line break
    print("\n")
    return letter_chars_location


# Function that checks that the string given contains the minimal characters needed for the program to work correctly
def min_input(raw_input, var_letter_library):
    count = 26
    for i in range(0, len(var_letter_library)):
        try:
            raw_input.index(var_letter_library[i])
            count -= 1
        except ValueError:
            pass
    if count == 26:
        return False
    else:
        return True


# Function that finds letter order in alphabet and returns it
def letter_order(letter, var_letter_library):
    return var_letter_library.index(letter.lower())+1


# Function that encodes text using key
def encode_text(var_text, var_letter_indexes, var_key, var_letter_library):
    # convert var_text to list
    var_text_list = list(var_text)
    # Set variable equal to number of letters (chars to encrypt/decrypt)
    num_of_valid_chars = len(var_letter_indexes)
    # repeat loop as many time as there are letters in the string
    for i in range(0, num_of_valid_chars):
        current_char = var_text_list[var_letter_indexes[i]]
        try:
            letter_index = var_letter_library.index(current_char)
            # letter is now known to be lowercase
            # replace original character with new encrypted character
            calling_index = (letter_index+var_key) % 26
            new_char = var_letter_library[calling_index]
        except ValueError:
            # letter is now known to be uppercase
            letter_index = var_letter_library.index(current_char.lower())
            calling_index = (letter_index + var_key) % 26
            new_char = var_letter_library[calling_index].upper()
        var_text_list[var_letter_indexes[i]] = new_char
    # convert list back into a string
    encoded_text = ""
    for i in range(0, len(var_text_list)):
        encoded_text += var_text_list[i]
    # return encoded string to user
    return encoded_text


# Lists/variables
# english letters
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                     "t", "u", "v", "w", "x", "y", "z"]

# Main routine
# Main routine
letter_indexes = str_checker(letters)
print(letter_indexes)
