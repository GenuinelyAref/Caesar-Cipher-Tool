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


check_input = min_input("0383782", ["0", "b", "c"])
print(check_input)
