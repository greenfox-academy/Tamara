# - Create a function called `printer`
#   which prints the input parameters
#   (can have multiple number of arguments)


def printer(*args):
    return args


print(printer("Hello", "world", "print"))
