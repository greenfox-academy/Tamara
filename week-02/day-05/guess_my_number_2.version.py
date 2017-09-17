
from random import randint
x = randint(1, 100)
def check_number(life, given):
    if x < given:
        life -= 1
        print("It\'s too high! You have only " + str(life) + " life left!")
    elif x > given:
        life -= 1
        print("Too low. You have only " + str(life) + " life left!")
    else:
        print("Congratulations. You won!")
    return life


def random_number():
    life = 5
    given_number = 0
    print("Hello! I've the number between 1-100. You have 5 lives.")
    while not x == given_number and life > 0:
        given_number = int(input("Give me a number! "))
        life = check_number(life, given_number)
        if life == 0:
            print("The number was: " + str(x) + "\nGame over. You lost all of your life.")
        

random_number()


