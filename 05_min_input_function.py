# Minimal input checker function

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


# english letters
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                     "t", "u", "v", "w", "x", "y", "z"]
test_values = ["abcde", "some554numbers8329", "394234687", "some_;$*)%(-symbols", "{]^@$@$&)(*$><:?"]

for j in range(0, len(test_values)):
    check_input = min_input(test_values[j], letters)
    print("There is at least one letter in \"{}\": {}".format(test_values[j], check_input))
