# - Create a function called `factorio`
#   that returns it's input's factorial


def factorio(factorial):
    sum_fact = factorial
    for i in range(1, factorial):
        sum_fact *= i
    return sum_fact

print(factorio(5))

