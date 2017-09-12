# - Create an array variable named `s`
#   with the following content: `[1, 2, 3, 8, 5, 6]`
# - Change the 8 to 4
# - Print the fourth element

s = [1, 2, 3, 8, 5, 6]
s.insert(3, 4)
s.remove(8)
print(s[3])

s = [1, 2, 3, 8, 5, 6]
s[3] = 4
print(s[3])
