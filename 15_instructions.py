# display instructions for new users

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


def instructions(condition_met):
    instructions_text = "| To use this tool, you will need to have a very basic understanding of Caesar Ciphers.\n" \
                   "| If you are unfamiliar with the concept, I highly recommend visiting this website\n" \
                   "| (https://csfieldguide.org.nz/en/chapters/coding-encryption/substitution-ciphers/)\n" \
                   "| and reading CSFG's article on Caesar Ciphers. " \
                   "\n\n| This tool can encode/decode a text, with or without a given key. This program\n" \
                   "| contains an intelligent ""letter frequency analysis tool, that is capable of decoding\n" \
                   "| any text without a given key in the least theoretical possible number of steps. You\n" \
                   "| will be required to enter the following information:\n\n| 1) text (can contain numbers, " \
                   "punctuation etc...)\n| 2) a key (if you have one)\n| 3) whether you want to encode or decode\n"
    if not condition_met:
        print(instructions_text)
    else:
        print("\033[3mSkipping instructions >>\033[0m")


want_instructions = yes_no_checker("Have you used this program before?\nYes/no: ", "", "", "Please enter yes/no")
instructions(want_instructions)
