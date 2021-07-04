
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


for i in range(0, 5):
    user_input = yes_no_checker("Say either yes or no: ", "\033[3mYou said yes\033[0m", "\033[3mYou said no\033[0m",
                                "\033[3mThat is not a valid answer\033[0m\n")
    print("Input status: \033[1m{}\033[0m\n".format(user_input))
