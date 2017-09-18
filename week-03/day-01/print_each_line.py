# Write a program that opens a file called "my-file.txt", then prints
# each of lines form the file.
# If the program is unable to read the file (for example it does not exists),
# then it should print an error message like: "Unable to read file: my-file.txt"


try:
    fr = open("my-text.txt", "r")
    print(my_text.readlines())
except FileNotFoundError:
    print("Unable to read file: my-file.txt")
