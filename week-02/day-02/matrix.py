# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

matrix = []
size = 4
for i in range(size):
    row = []
    for j in range(size):
        if i == j:
            row.append("1")
        else:
            row.append("0")
    matrix.append(row)

for matrix_row in range(len(matrix)):
    print(matrix[matrix_row])