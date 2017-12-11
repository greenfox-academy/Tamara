# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4


def average_of_numbers():
    x = 0
    sum = 0
    average = 0
    counter = 0
    for i in range(0, 5):
        i = int(input("Give me a number! "))
        sum += i
        counter += 1
        average = float(sum/counter)
    print("Sum: " + str(sum) + ", Average: " + str(average))


average_of_numbers()
