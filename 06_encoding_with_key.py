# Encoding letters with a provided key

# string checker function
def str_checker(var_text, var_letter_library):
    var_text_lower = var_text.lower()
    letter_chars_location = []
    # check that all characters are valid/permitted
    for i in range(0, len(var_text_lower)):
        current_char = var_text_lower[i]
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


def encode_with_key(var_text, var_letter_indexes, var_key, var_letter_library):
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


# english letters
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                     "t", "u", "v", "w", "x", "y", "z"]
text = "? special ! characters _ + ="
key = 26

# Main routine
x = str_checker(text, letters)
b = encode_with_key(text, x, key, letters)
print("The text \033[1m\"{}\"\033[0m encrypted using a key of \033[1m{}\033[0m is: \033[1m\"{}\"\033[0m"
      .format(text, key, b))
