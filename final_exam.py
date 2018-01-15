# 1. exercise
# Create a function that takes a matrix (list of lists) of numbers
# and sums all the numbers.

list_of_numbers = [[4, 6, 10], [3, 5, 7]]


def sum_numbers():
    total_of_numbers = 0
    for i in range(len(list_of_numbers)):
        for num in range(len(list_of_numbers[i])):
            total_of_numbers += list_of_numbers[i][num]
    return total_of_numbers


print(sum_numbers())


# other solution

def sum_other_numbers(list_of_nums):
    sum_of_num = 0
    for row in range(len(list_of_nums)):
        for num in range(len(list_of_nums[row])):
            sum_of_num += list_of_nums[row][num]
    return sum_of_num


print(sum_other_numbers([[1, 2], [3, 4]]))
