def letter_frequency(text):
    # english letters
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
               "t", "u", "v", "w", "x", "y", "z"]

    var_text = text.lower()
    letter_frequency_dict = {}
    for i in var_text:
        keys = letter_frequency_dict.keys()
        try:
            letters.index(i)
            if i in keys:
                letter_frequency_dict[i] += 1
            else:
                letter_frequency_dict[i] = 1
        except ValueError:
            pass
    return letter_frequency_dict


text = "He had three simple rules by which he lived. The first was to never eat blue food. There was nothing in " \
       "nature that was edible that was blue. People often asked about blueberries, but everyone knows those are " \
       "actually purple. He understood it was one of the stranger rules to live by, but it had served him well thus " \
       "far in the 50+ years of his life. "
print(letter_frequency(text))
