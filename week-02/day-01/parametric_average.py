# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4



def sum_and_average():
    counter = 0
    sum = 0
    average = 0
    x = 0
    while sum < 100:
        x = int(input("Give me a number! "))
        sum += x
        counter += 1
        average = sum/counter
    
        print("Sum: " + str(sum) + ", Average: " + str(average))


sum_and_average()

    