# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was
N = int(input("Give me a number! "))
stars = 0
for i in range(N):
    if i < N/2:
        stars = i * 2 + 1
    else:
        stars = ((N - 1 - i) * 2 + 1)
    spaces = int((N - stars)/2)
    print(' ' * spaces + '*' * stars + ' ' * spaces)


