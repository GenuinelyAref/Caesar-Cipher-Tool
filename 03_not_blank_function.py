# blank checking function
def not_blank(prompt, error_message):
    user_input = input(prompt)
    while user_input.strip(" ") == "":
        print("{}\n".format(error_message))
        user_input = input(prompt)
    return user_input


age = not_blank("How old are you? Enter here: ", "You cannot leave this blank, try again")
