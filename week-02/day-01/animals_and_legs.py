# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The second represents the number of pigs the farmer has
# It should print how many legs all the animals have


def sum_all_legs():
    chicken = int(input("How many chicken have you got? "))
    pig = int(input("How many pig have you got? "))
    sum = chicken * 2 + pig * 4
    return "Altogether animals have " + str(sum) + " legs."


print(sum_all_legs())
    