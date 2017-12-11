# Write a program that asks for two numbers and prints the bigger one
a = int(input("Give me a number! "))
b = int(input("Give me a number! "))

def bigger_number():
    if a > b :
        return a
    elif b > a:
        return b

print(bigger_number())
