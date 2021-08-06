# Caesar Cipher Tool

# LIBRARIES
import random


# FUNCTIONS
# random key-picking function
def random_key_pick():
    return random.randint(1, 25)


# integer checker for cipher key value
def integer_check(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


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
def str_checker(var_text, var_letter_library):
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
    return letter_chars_location


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


# Function that calculates the likelihood of the outcome
def likelihood_of_outcome(letter, var_standard_letters, var_standard_values):
    var_index = var_standard_letters.index(letter)
    var_sum = 0
    for i in range(0, var_index + 1):
        var_sum += var_standard_values[i]
    return round(100 - var_sum, 3)


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
    return [encoded_text, var_key]


# Function to decode text using key
def decode_text(var_text, var_letter_indexes, var_key, var_letter_library):
    # convert var_text to list
    var_text_list = list(var_text)
    # Set variable equal to number of letters (chars to decrypt/decrypt)
    num_of_valid_chars = len(var_letter_indexes)
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
    decoded_text = ""
    for i in range(0, len(var_text_list)):
        decoded_text += var_text_list[i]
    # return decoded string to user
    return [decoded_text, var_key]


# Function to decode text using key
def decode_without_key(var_text, var_letter_indexes, var_letter_library, var_most_frequent_letter,
                       var_standard_freq_letters):
    decoded_text = ""
    var_key = 0
    # Set variable equal to number of letters (chars to decrypt/decrypt)
    num_of_valid_chars = len(var_letter_indexes)
    # decoding without key part:
    correct = False
    letter_count = 0
    while not correct:
        a = var_letter_library.index(var_most_frequent_letter)
        b = var_letter_library.index(var_standard_freq_letters[letter_count])
        var_key = (26 - (b - a)) % 26
        letter_count += 1
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
        decoded_text = ""
        for i in range(0, len(var_text_list)):
            decoded_text += var_text_list[i]
        correct_key = yes_no_checker("Is this the correct text?\033[1m\n{}\033[0m\n\nYes/no: ".format(decoded_text),
                                     "Success!", "\n\033[3mtrying again\033[0m\n", "Please enter yes/no")
        if correct_key:
            break
        else:
            continue
    # return decoded string to user
    return [decoded_text, var_key]


# Program instructions
def instructions(condition_met):
    instructions_text = " | To use this tool, you will need to have a very basic understanding of Caesar Ciphers.\n" \
                   " | If you are unfamiliar with the concept, I highly recommend visiting this website\n" \
                   " | (https://csfieldguide.org.nz/en/chapters/coding-encryption/substitution-ciphers/)\n" \
                   " | and reading CSFG's article on Caesar Ciphers. " \
                   "\n\n | This tool can encode/decode a text, with or without a given key. This program\n" \
                   " | contains an intelligent ""letter frequency analysis tool, that is capable of decoding\n" \
                   " | any text without a given key in the least theoretical possible number of steps. You\n" \
                   " | will be required to enter the following information:\n\n | 1) text (can contain numbers, " \
                   "punctuation etc...)\n | 2) a key (if you have one)\n | 3) whether you want to encode or decode"
    if not condition_met:
        print(instructions_text)
    else:
        print("\033[3mSkipping instructions >>\033[0m")


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
user_input= ""
key = 0

# MAIN ROUTINE

# welcome message
print("\033[1mWelcome to Caesar Cipher Tool\033[0m\n\n\n\n")
# display/skip instructions
want_instructions = yes_no_checker("Have you used this program before?\nYes/no: ", "", "", "Please enter yes/no")
instructions(want_instructions)

# Check that there is something to encode/decode
user_text_valid = False
# If not, then keep requesting new text
while not user_text_valid:
    # explain why the prompt is repeated
    print("\n\n\033[3mPlease ensure that your text contains at least 1 letter\033[0m")
    # repeat prompt
    user_input = input("Enter you text here: ")
    # check that the text contains at least one letter
    user_text_valid = min_input(user_input, letters)

# Ask user if they want to encode or decode
text_function = input("\n\033[1mDo you want to encode or decode?\033[0m\nType here: ")
# If answer is not valid, ask again
while text_function.lower() != "encode" and text_function.lower() != "decode":
    # error saying why it's invalid
    print("\nSorry, that is not a valid answer. Type 'encode' or 'decode'\n")
    # repeat prompt
    text_function = input("\033[1mDo you want to encode or decode?\033[0m\nType here: ")
# change the function to lowercase
text_function = text_function.lower()

# Ask if user has key
user_has_key = yes_no_checker("\n\033[1mDo you have a key to provide?\033[0m\nYes/no: ", "",
                              "\n\033[3mNo key given\033[0m", "Please enter yes/no")

# If user has key, ask them for it
if user_has_key:
    valid_key = False
    while not valid_key:
        print("\n\033[3mMake sure your key is an integer\033[0m")
        key = input("Enter your key here: ")
        valid_key = integer_check(key)
    key=int(key)


if text_function == "decode":
    if user_has_key:
        result = decode_text(user_input, str_checker(user_input, letters), key, letters)
    else:
        result = decode_without_key(user_input, str_checker(user_input, letters), letters, letter_frequency(user_input, letters), standard_freq_letters)
    print("\n\033[1mKey: \033[0m\033[3m{}\033[0m\n\n\033[0m\033[1mOriginal text:\033[0m\n\033[3m{}\033[0m\n\n\033["
          "1mDecoded text:\033[0m\n\033[3m{}\033[0m".format(result[1], user_input, result[0]))
else:
    if user_has_key:
        result = encode_text(user_input, str_checker(user_input, letters), key, letters)
    else:
        key = random_key_pick()
        print("\033[3mRandom key generated\033[0m")
        result = encode_text(user_input, str_checker(user_input, letters), key, letters)
    print("\n\033[1m | Key: \033[0m\033[3m{}\033[0m\n\n\033[0m\033[1m | Original text:\033[0m\n\033[3m{}\033[0m\n\n\033["
          "1m | Encoded text:\033[0m\n\033[3m{}\033[0m".format(result[1], user_input, result[0]))
