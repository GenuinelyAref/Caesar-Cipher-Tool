# Standard letter frequency table (letters)
standard_freq_letters = ["e", "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y", "p",
                         "b", "v", "k", "j", "x", "q", "z"]
# Standard letter frequency table (values)
standard_freq_values = [12.702, 9.056, 8.167, 7.507, 6.966, 6.749, 6.327, 6.094, 5.987, 4.253, 4.025, 2.782, 2.758,
                        2.406, 2.36, 2.228, 2.015, 1.974, 1.929, 1.492, 0.978, 0.772, 0.153, 0.15, 0.095, 0.074]

for i in range(0, len(standard_freq_letters)):
    print("The frequency of the letter {} is {}%".format(standard_freq_letters[i], standard_freq_values[i]))
