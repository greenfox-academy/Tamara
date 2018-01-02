# Crate a program that draws a chess table like this
#
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
#
N = 8


def chess_table():
    for i in range(N):
        if i % 2 == 0:
            print(int(N/2) * "% ")
        else:
            print(int(N/2) * " %")


chess_table()
