# - Create a variable named `ai`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Print the sum of the elements in `ai`

ai = [3, 4, 5, 6, 7]

def sum(ai):
    summa = 0
    for i in ai:
        summa += i
    return summa

print(sum(ai))