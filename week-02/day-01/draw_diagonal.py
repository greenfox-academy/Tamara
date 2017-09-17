# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was
N = int(input("Give me a number! "))

def square():
    for i in range(N):
        if i == 0 or i == (N-1):
            print("%" * N)
        else:
            print("%" + (i-1)* " " + "%" + (N-2-i) * " " + "%")

square()
