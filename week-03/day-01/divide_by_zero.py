# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

def divide():
    divisor = int(input("Give me a number! "))
    try:
        result = 10 / divisor
        print(str(result))
    except ZeroDivisionError:
        print("Fail")
    except ValueError:
        print("It must be an integer")

divide()