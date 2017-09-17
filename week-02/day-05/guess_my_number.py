from random import randint


#print(randint(1, 50))

def guess_number():
    x = randint(1, 100)
    guess_number = -1
    life = 5
    print("Hello! I've the number between 1-100. You have 5 lives.")
    while not x == guess_number and life > 0:
        guess_number = int(input("Give me a new number! "))
        if x == guess_number:
            print("Congratulations! You won!")
        elif x > guess_number:
            life -= 1
            print("Too low. You have only " + str(life) + " life left.")
        elif x < guess_number:
            life -= 1
            print("Too high.You have only " + str(life) + " life left.")


guess_number()
