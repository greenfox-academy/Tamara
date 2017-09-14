# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

number = int(input("Write a number! "))
for i in range(number):
    print("*" * (i + 1))

# with list:
# stars = 0
# def triangle(stars):
#     star = []
#     size = 4
#     for i in range(size):
#         row = []
#         for j in range(size):
#             if j == i:
#                  row.append("*")
#             elif j < i:
#                 row.append("*")
#             else:
#                 row.append(" ")
#         star.append(row)

#     for triangle_row in range(len(star)):
#         print(star[triangle_row])

# triangle(stars)


        
