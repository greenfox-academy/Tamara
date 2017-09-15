# Create a program that prints all the even numbers between 0 and 500

a = 0
for a in range(0, 501):
    if a % 2 == 0:
        print(a)
        a += 1