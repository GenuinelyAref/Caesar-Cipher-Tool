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


# main routine
age = not_blank("How old are you? Enter here: ", "You cannot leave this blank, try again")
