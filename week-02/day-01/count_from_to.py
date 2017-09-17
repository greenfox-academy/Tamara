# Create a program that asks for two numbers
# If the second number is not bigger than the first one it should print:
# "The second number should be bigger"
#
# If it is bigger it should count from the first number to the second by one
# 
# example:
#
# first number: 3, second number: 6, should print:
#
# 3
# 4
# 5

#user_input = ("Please, give a number!" )
#user_input = ("Please, give another number!" )

x = int(input("Please, give a number!" ))
y = int(input("Please, give another number!" ))
def counter(x, y):
    if x > y:
        print("The second number should be bigger")
    else:
        while x < y:
            print(x)
            x += 1       
counter(x, y)