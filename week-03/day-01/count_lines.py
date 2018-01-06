# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

file_name = input("Give me a filename! ")


def count_lines(file_name):
    try:
        lines = 0
        for line in open(file_name):
            lines += 1
        return lines
    except FileNotFoundError:
        return 0


print(count_lines(file_name))
