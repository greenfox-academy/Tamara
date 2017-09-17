# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8


number = 8
def guess_number():
    x = 0
    while x != number:
        x = int(input("Guess a number! "))
        if x < number:
            print("The stored number is higher")
        elif x > number:
            print("The stored number is lower")
    
    print("You found the number: " + str(number))

guess_number()