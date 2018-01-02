# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

need_to_contain = [4, 8, 12, 16]


def is_all_element_in_the_list(list_of_numbers):
    for element in need_to_contain:
        if element not in list_of_numbers:
            return False
    return True


print(is_all_element_in_the_list([2, 4, 6, 8, 10, 12, 14, 16]))
