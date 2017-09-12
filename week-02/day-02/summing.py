# - Write a function called `sum` that sum all the numbers
#   until the given parameter


numbers = [1, 2, 3, 4, 5]
def sum (numbers):
    num_sum = 0
    for i in numbers:
        num_sum += i
    return num_sum
    
print(sum(numbers))
