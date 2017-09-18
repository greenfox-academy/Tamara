# Create a function that takes 3 parameters: a path, a word and a number,
# than it should write to a file.
# The path parameter should be a string, that describes the location of the file.
# The word parameter should be a string, that will be written to the file as lines
# The number paramter should describe how many lines the file should have.
# So if the word is "apple" and the number is 5, than it should write 5 lines
# to the file and each line should be "apple"
# The function should not raise any error if it could not write the file.

import os.path

def write_multiple_lines(path, word, number):
    multiple_line = open(os.path.join("multiple_line.txt"), "w")
    try:
        for word in range(number):
            multiple_line.write(word + "\n")
    except:
        return 0


write_multiple_lines("D:\greenfox\first-task\Tamara\week-03\day-01", "apple", 5)