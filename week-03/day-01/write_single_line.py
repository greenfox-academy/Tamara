# Open a file called "my-file.txt"
# Write your name in it as a single line
# If the program is unable to write the file,
# then it should print an error message like: "Unable to write file: my-file.txt"

def write_single_line(filename):
    try:
        fw = open(filename, 'w')
        fw.write('Tamara')
    except IOError:
        return 'Unable to write file: my-file.txt'


print(write_single_line('my-file.txt'))
