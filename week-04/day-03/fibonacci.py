# # Fibonacci
# - Write a function that computes a member of the fibonacci sequence by a given index
# - Create tests that covers all types of input (like in the previous workshop exercise)

def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)
