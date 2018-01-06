# Create a method that find the 5 most common lottery numbers otos.csv
import csv

csv_file = open('otos.csv', 'r')
content = csv.reader(csv_file, delimiter=';')
num_list = []
last_five_slice = slice(-5, None)


def all_lottery_numbers():
    for row in content:
        for num in row[last_five_slice]:
            num_list.append(num)
    return num_list


def five_most_frequented_numbers():
    all_lottery_numbers()
    counted = {}
    for num in num_list:
        if num in counted:
            counted[num] += 1
        else:
            counted[num] = 0
    result = [(key, counted[key]) for key in sorted(counted, key=counted.get, reverse=True)][:5]
    return result


print(five_most_frequented_numbers())
