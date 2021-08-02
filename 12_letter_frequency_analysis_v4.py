# Tool to calculate the frequency of each letter in any string

def letter_frequency(text, var_letter_library):
    var_text = text.lower()
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


# english letters
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
           "t", "u", "v", "w", "x", "y", "z"]


n = "The robot clicked disapprovingly, gurgled briefly inside its cubical interior and extruded a pony glass of " \
    "brownish liquid. \"Sir, you will undoubtedly end up in a drunkard's grave, dead of hepatic cirrhosis," \
    "\" it informed me virtuously as it returned my ID card. I glared as I pushed the glass across the table. "

most_frequent_letter = letter_frequency(n, letters)

print("Most frequent letter: {}".format(most_frequent_letter))
