# - Create a variable named `af`
#   with the following content: `[4, 5, 6, 7]`
# - Print all the elements of `af`

af = [4, 5, 6, 7]
for i in af:  # with this solution print the lements in a column
    print(i)

# or

print(af)  # with this solution print the lements in a list in one line

# or

print_in_row = ""   # With this solution print the elements in a row
for i in af:
    print_in_row += str(i)
    print_in_row += " "
print(print_in_row)
