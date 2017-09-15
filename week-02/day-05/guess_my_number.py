from random import randint


#print(randint(1, 50))

def guess_number():
    x = randint(1, 10)
    guess_number = -1
    life = 5
    while not x == guess_number and life > 0:
        guess_number = int(input("Give me a new number! "))
        if x == guess_number:
            print("Yupppii")
        elif x > guess_number:
            life -= 1
            print("Too low.")
        elif x < guess_number:
            life -= 1
            print("too high")


guess_number()
