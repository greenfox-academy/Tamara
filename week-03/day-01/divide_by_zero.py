# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

divisor = input("Give me a number! ")


def divide():
    try:
        result = 10 / int(divisor)
        return result
    except ZeroDivisionError:
        return "Fail"
    except ValueError:
        return "It must be an integer"


print(divide())
