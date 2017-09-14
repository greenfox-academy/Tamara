
students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints: 
#  - how many candies they have on average

def name_counter(students):
    names = 0
    for student in students:
        if student['candies'] > 4:
            names = student['name']
    return names
print(name_counter(students))

def average():
    avg = 0
    for i in range(len(students)):
        avg += students[i]['candies']/len(students)
    return(avg)

print(average())