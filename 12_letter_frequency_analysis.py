# Tool to calculate the frequency of each letter in any string

def frequency_analysis(text, var_letter_library):
    letter_frequencies = []
    var_text = text.lower()
    for i in range(0, len(var_text)):
        try:
            var_index = var_text[i].index(var_letter_library)




