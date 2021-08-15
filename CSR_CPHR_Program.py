# Caesar Cipher Tool

# LIBRARIES
import random


# FUNCTIONS
# random key-picking function - for encoding without key
def random_key_pick():
    return random.randint(1, 25)


# integer checker for cipher key value - to check that key is valid/usable
def integer_check(var_num):
    try:
        # try converting value into integer
        int(var_num)
        # if successful then given value is an integer
        return True
    except ValueError:
        # if not successful then given value cannot be an integer (string, float etc..)
        return False


# function that strips leading/trailing spaces from an input
def strip_spaces(var_text):
    return var_text.strip(" ")


# string checker function - returns the positions of all decryptable/encryptable characters
def letter_position_finder(var_text, var_letter_library):
    # change all letters in the string to lowercase
    var_text = var_text.lower()
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
    # return all the positions of the letters in the string
    return letter_chars_location


# Function that checks that input given is either yes or no - repeats prompt if neither answer is given
def yes_no_checker(var_prompt, var_proceed_affirmative, var_proceed_negative):
    valid_two = False
    # repeat until answer given is either 'yes' or 'no'
    while not valid_two:
        # ask question
        answer = strip_spaces(input(var_prompt))
        # change all letters in the string to lowercase
        answer = answer.lower()
        if answer == "yes" or answer == "y":
            # print matching statement
            print(var_proceed_affirmative)
            return True
        elif answer == "no" or answer == "n":
            # print matching statement
            print(var_proceed_negative)
            return False
        else:
            # print error message + don't exit loop
            print("\n\033[3mPlease enter yes/no\033[0m")


# Function that checks that the string given contains the minimal characters needed for the program to work correctly
def min_input(var_raw_input, var_letter_library):
    count = 26
    # repeat loop for each character in the string
    for i in range(0, len(var_letter_library)):
        try:
            # try to index the character in the letter library
            var_raw_input.index(var_letter_library[i])
            # if successful then change the count variable
            count -= 1
        except ValueError:
            # if unsuccessful then keep the count variable the same
            pass
    # if count is unchanged then there are no letters in the given string
    if count == 26:
        return False
    # if count has changed then there are one or more letters in the given string
    else:
        return True


# Function that finds letter order in alphabet and returns it
def letter_order(var_letter, var_letter_library):
    return var_letter_library.index(var_letter.lower()) + 1


# Function that calculates the likelihood of the outcome
def likelihood_of_outcome(var_letter, var_standard_letters, var_standard_values):
    # Find the order of the letter in the standard letter frequency table
    var_index = var_standard_letters.index(var_letter)
    percentage = var_standard_values[var_index]
    return percentage


# Letter frequency analysis tool
def letter_frequency(var_text, var_letter_library):
    var_text = var_text.lower()
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


# Function that encodes text using key
def encode_decode_with_key(var_text, var_letter_indexes, var_key, var_letter_library):
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
            calling_index = (letter_index + var_key) % 26
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
    # make sure printed key is positive after decoding
    if var_key < 0:
        var_key = abs(var_key)
    # return encoded string to user
    return [encoded_text, var_key]


# Function to decode text using key
def decode_without_key(var_text, var_letter_indexes, var_letter_library, var_most_frequent_letter,
                       var_standard_freq_letters):
    decoded_text = ""
    var_key = 0
    # Set variable equal to number of letters (chars to decrypt/decrypt)
    num_of_valid_chars = len(var_letter_indexes)
    correct = False
    letter_count = -1
    # find index of the most frequent letter
    most_frequent_letter_index = var_letter_library.index(var_most_frequent_letter)
    # repeat until user claims that the string is decoded correctly
    while not correct:
        letter_count += 1
        decoded_text = ""
        # find index of the next-most frequent letter's index in the standard letter frequency table
        next_most_standard_frequent_letter_index = var_letter_library.index(var_standard_freq_letters[letter_count])
        # set the key equal to the difference between both indexes
        var_key = (26 - (next_most_standard_frequent_letter_index - most_frequent_letter_index)) % 26
        # to increase the progression of standard letter table values
        # convert var_text to list
        var_text_list = list(var_text)
        # repeat loop as many time as there are letters in the string
        for i in range(0, num_of_valid_chars):
            current_char = var_text_list[var_letter_indexes[i]]
            try:
                letter_index = var_letter_library.index(current_char)
                # letter is now known to be lowercase
                # replace original character with new decrypted character
                calling_index = (letter_index - var_key) % 26
                new_char = var_letter_library[calling_index]
            except ValueError:
                # letter is now known to be uppercase
                letter_index = var_letter_library.index(current_char.lower())
                calling_index = (letter_index - var_key) % 26
                new_char = var_letter_library[calling_index].upper()
            var_text_list[var_letter_indexes[i]] = new_char
        # convert list back into a string
        for i in range(0, len(var_text_list)):
            decoded_text += var_text_list[i]
        correct_key = yes_no_checker("Is this the correct text?\033[1m\n{}\033[0m\n\nYes/no: ".format(decoded_text),
                                     "Success!", "\033[3m\ntrying again\033[0m\n")
        # if decoded text is claimed correct by the user, break loop
        if correct_key:
            break
        # if decoded text is incorrect, continue loop
        else:
            continue
    # return decoded string to user
    return [decoded_text, var_key, var_standard_freq_letters[letter_count]]


# Program instructions
def instructions(var_condition_met):
    instructions_text = "\033[1m | Here's a basic set of instructions on how to use this program: \033[0m\n\n" \
                        " | To use this tool, you will need to have a very basic understanding of Caesar Ciphers.\n" \
                        " | If you are unfamiliar with the concept, I highly recommend visiting this website\n" \
                        " | (https://csfieldguide.org.nz/en/chapters/coding-encryption/substitution-ciphers/)\n" \
                        " | and reading CSFG's article on Caesar Ciphers. " \
                        "\n\n | This tool can encode/decode a text, with or without a given key. This program\n" \
                        " | contains an intelligent ""letter frequency analysis tool, that is capable of decoding\n" \
                        " | any text without a given key in the least theoretical possible number of steps. You\n" \
                        " | will be required to enter the following information:\n\n | 1) text (can contain numbers, " \
                        "punctuation etc...)\n | 2) a key (if you have one)\n | 3) whether you want to encode or decode"
    if not var_condition_met:
        print(instructions_text)
    else:
        print("\033[3mSkipping instructions >>"
              "\n\n"
              "If you wish to re-read the instructions, please see the README file for this repository\033[0m")


# Lists/variables
# english letters
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
           "t", "u", "v", "w", "x", "y", "z"]
# Standard letter frequency table (letters)
standard_freq_letters = ["e", "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y", "p",
                         "b", "v", "k", "j", "x", "q", "z"]
# Standard letter frequency table (values)
standard_freq_values = [12.702, 9.056, 8.167, 7.507, 6.966, 6.749, 6.327, 6.094, 5.987, 4.253, 4.025, 2.782, 2.758,
                        2.406, 2.36, 2.228, 2.015, 1.974, 1.929, 1.492, 0.978, 0.772, 0.153, 0.15, 0.095, 0.074]
user_input = ""
key = 0

# MAIN ROUTINE

# welcome message
print("\033[1mWelcome to Caesar Cipher Tool\033[0m\n\n\n\n")
# display/skip instructions
want_instructions = yes_no_checker("Have you used this program before?\nYes/no: ", "", "")
instructions(want_instructions)

want_to_run_program_again = True
while want_to_run_program_again:
    # Check that there is something to encode/decode
    user_text_valid = False
    # If not, then keep requesting new text
    while not user_text_valid:
        # explain why the prompt is repeated
        print("\n\n\033[3mPlease ensure that your text contains at least 1 letter\033[0m")
        # repeat prompt
        user_input = strip_spaces(input("Enter you text here: "))
        # check that the text contains at least one letter
        user_text_valid = min_input(user_input, letters)

    # Ask user if they want to encode or decode
    text_function = strip_spaces(input("\n\033[1mDo you want to encode or decode?\033[0m\nType here: "))
    # If answer is not valid, ask again
    while text_function.lower() != "encode" and text_function.lower() != "decode" and text_function.lower() != "e"\
            and text_function.lower() != "d":
        # error saying why it's invalid
        print("\n\033[3mSorry, that is not a valid answer. Type 'encode' or 'decode'\033[0m\n")
        # repeat prompt
        text_function = strip_spaces(input("\033[1mDo you want to encode or decode?\033[0m\nType here: "))
    # change the function to lowercase
    text_function = text_function.lower()
    if text_function == "e":
        text_function = "encode"
    elif text_function == "d":
        text_function = "decode"
    # print the function the user chose for confirmation
    print("\n\033[3mYou chose to <{}>\033[0m".format(text_function))

    # Ask if user has key
    user_has_key = yes_no_checker("\n\033[1mDo you have a key to provide?\033[0m\nYes/no: ", "",
                                  "\n\033[3mNo key given\033[0m")
    # If user has key, ask them for it
    if user_has_key:
        valid_key = False
        while not valid_key:
            print("\n\033[3mMake sure your key is an integer\033[0m")
            key = strip_spaces(input("Enter your key here: "))
            valid_key = integer_check(key)
        key = int(key)

    # is user wants to decode text
    if text_function == "decode":
        # if user has key
        if user_has_key:
            # use general encode/decode function
            result = encode_decode_with_key(user_input, letter_position_finder(user_input, letters), -key, letters)
            extra_text = ""
        # if user doesn't have key
        else:
            # use special function
            result = decode_without_key(user_input, letter_position_finder(user_input, letters), letters,
                                        letter_frequency(user_input, letters), standard_freq_letters)
            likelihood = likelihood_of_outcome(result[2], standard_freq_letters, standard_freq_values)
            extra_text = "\n\n" \
                         " \033[1m| Likelihood of outcome: \033[0m\033[3m{}%\033[0m".format(likelihood)
        # print results
        print("\n\033[1m | Key: \033[0m\033[3m{}\033[0m"
              "\n\n"  # line break
              " \033[1m| Original text:\033[0m\n | \033[3m{}\033[0m"
              "\n\n"  # line break
              " \033[1m| Decoded text:\033[0m\n | \033[3m{}\033[0m"
              "{}"
              .format(result[1], user_input, result[0], extra_text))
    # is user wants to encode text
    else:
        # if user has key
        if user_has_key:
            # user general encode/decode function
            result = encode_decode_with_key(user_input, letter_position_finder(user_input, letters), key, letters)
        # if user doesn't have key
        else:
            # pick random key
            key = random_key_pick()
            print("\033[3mRandom key generated\033[0m")
            # use general encode/decode function
            result = encode_decode_with_key(user_input, letter_position_finder(user_input, letters), key, letters)
        # print results
        print("\n\033[1m | Key: \033[0m\033[3m{}\033[0m"  # print key
              "\n\n"  # line break
              " \033[1m| Original text:\033[0m\n | \033[3m{}\033[0m"  # print original text
              "\n\n"  # line break
              " \033[1m| Encoded text:\033[0m\n | \033[3m{}\033[0m"  # print encoded text
              .format(result[1], user_input, result[0]))
    want_to_run_program_again = yes_no_checker("\n\n\033[1mDo you want to run this program again?\033[0m\nYes/no: ",
                                               "\n\033[3mRe-running program\033[0m",
                                               "\n\033[3mThank you for using my program :)\033[0m")
