# # Count Letters
#  - Write a function, that takes a string as an argument and returns a
# dictionary with all letters in the string as keys, and numbers as values
# that shows how many occurrences there are.
#  - Create a test for that.


def letter_counter(word):
    counted_letters = {}
    for letter in word:
        if letter in counted_letters:
            counted_letters[letter] += 1
        else:
            counted_letters[letter] = 1
    return counted_letters
