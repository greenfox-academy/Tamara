
from random import randint


x = randint(1, 100)
life = 5
print("Hello! I've the number between 1-100. You have 5 lives.")
given_number = int(input("Give me a number! "))
left_life = life - 1

def life_counter(): 
    life = 5
    if life == 0:
        print("You lost all life. Game over")
    elif x != given_number:
        left_life = life - 1
        print("You lost one life")
    return life

def random_number(x):
    if x < given_number:
        print("It\'s too high! You have only " + str(life) + " life left!")
        input("Give me a new number! ")
        return given_number
    elif x > given_number:
        print("Too low. You have only " + str(life) + " life left!")
        input("Give me a new number! ")   

left_life = life - 1
total_left_life = left_life - 1    
def finding_number(total_left_life):
    while total_left_life > 0:
        life_counter()
        searched_number = random_number(x)
        if given_number == x:
            life_counter()
            searched_number
            print("Congratulations. You won!")
        else:
            life_counter()
            random_number(x)
            return searched_number
    return total_left_life

print(finding_number(left_life))