# Decoding letters without a provided key (complex analysis tool)


# Function that checks that input given is either yes or no
def yes_no_checker(prompt, proceed_affirmative, proceed_negative, error_message):
    valid_two = False
    while not valid_two:
        answer = input(prompt)
        answer = answer.lower()
        if answer == "yes":
            print(proceed_affirmative)
            return True
        elif answer == "no":
            print(proceed_negative)
            return False
        else:
            print(error_message)


# Function that calculates the likelihood of the outcome
def likelihood_of_outcome(letter, var_standard_letters, var_standard_values):
    var_index = var_standard_letters.index(letter)
    var_sum = 0
    for i in range(0, var_index + 1):
        var_sum += var_standard_values[i]
    return round(100 - var_sum, 3)


# Letter frequency analysis tool
def letter_frequency(textt, var_letter_library):
    var_text = textt.lower()
    letter_frequency_dict = {}
    for i in var_text:
        keys = letter_frequency_dict.keys()
        try:
            var_letter_library.index(i)
            if i in keys:
                letter_frequency_dict[i] += 1
            else:
                letter_frequency_dict[i] = 1
        except ValueError:
            pass
    letter_frequency_dict = sorted(letter_frequency_dict.items(), key=lambda x: x[1], reverse=True)
    letter_frequency_dict = dict(letter_frequency_dict)
    letter_list = list(letter_frequency_dict.keys())
    return letter_list[0]


# string checker function
def str_checker(var_text, var_letter_library):
    var_text_lower = var_text.lower()
    letter_chars_location = []
    # check for all decrypt-able characters (letters)
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


# Function to decode text using key
def decode_without_key(var_text, var_letter_indexes, var_letter_library, var_most_frequent_letter,
                       var_standard_freq_letters):
    decoded_text = ""
    # Set variable equal to number of letters (chars to decrypt/decrypt)
    num_of_valid_chars = len(var_letter_indexes)

    # decoding without key part:
    correct = False
    letter_count = 0
    while not correct:
        a = var_letter_library.index(var_most_frequent_letter)
        b = var_letter_library.index(var_standard_freq_letters[letter_count])
        var_key = 26-(b-a)
        letter_count += 1
        # STOPPED HERE
        # ######################
        # convert var_text to list
        var_text_list = list(var_text)
        # repeat loop as many time as there are letters in the string
        for i in range(0, num_of_valid_chars):
            current_char = var_text_list[var_letter_indexes[i]]
            try:
                letter_index = var_letter_library.index(current_char)
                # letter is now known to be lowercase
                # replace original character with new decrypted character
                calling_index = ((letter_index) -(var_key)) % 26
                new_char = var_letter_library[calling_index]
            except ValueError:
                # letter is now known to be uppercase
                letter_index = var_letter_library.index(current_char.lower())
                calling_index = ((letter_index) -(var_key)) % 26
                new_char = var_letter_library[calling_index].upper()
            var_text_list[var_letter_indexes[i]] = new_char
        # convert list back into a string
        decoded_text = ""
        for i in range(0, len(var_text_list)):
            decoded_text += var_text_list[i]
        correct_key = yes_no_checker("Is this the correct text?\n\n{}".format(decoded_text), "yay",
                                     "oops, trying again", "Please enter yes/no")
        if correct_key:
            break
        else:
            continue
    # return decoded string to user
    return decoded_text


# english letters
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
           "t", "u", "v", "w", "x", "y", "z"]

# Standard letter frequency table (letters)
standard_freq_letters = ["e", "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y", "p",
                         "b", "v", "k", "j", "x", "q", "z"]

# Standard letter frequency table (values)
standard_freq_values = [12.702, 9.056, 8.167, 7.507, 6.966, 6.749, 6.327, 6.094, 5.987, 4.253, 4.025, 2.782, 2.758,
                        2.406, 2.36, 2.228, 2.015, 1.974, 1.929, 1.492, 0.978, 0.772, 0.153, 0.15, 0.095, 0.074]

# message (key = 13)
text = "f xvzfwji uqzx g xvzfwji jvzfqx h xvzfwji"
text_letter_locations = str_checker(text, letters)

# Main routine
# likelihood of outcome (= 0.17%)
likelihood = likelihood_of_outcome("x", standard_freq_letters, standard_freq_values)
# find most frequent letter in the text
most_frequent_letter = letter_frequency(text, letters)
# try to decode the key
n = decode_without_key(text, text_letter_locations, letters, most_frequent_letter, standard_freq_letters)
print(n)
