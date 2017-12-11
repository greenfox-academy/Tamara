# Write a program that asks for two numbers and prints the bigger one
a = int(input("Give me a number! "))
b = int(input("Give me a number! "))

def bigger_number():
    if a > b :
        print(a)
    elif b > a:
        print(b)

bigger_number()
