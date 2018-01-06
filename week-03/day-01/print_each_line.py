# Write a program that opens a file called "my-file.txt", then prints
# each of lines form the file.
# If the program is unable to read the file (for example it does not exists),
# then it should print an error message like: "Unable to read file: my-file.txt"

def print_each_lines(filename):
    try:
        fr = open(filename, "r")
        return fr.read()
    except FileNotFoundError:
        return "Unable to read file: my-file.txt"


print(print_each_lines("my-file.txt"))
