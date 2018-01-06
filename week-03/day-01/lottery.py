# Create a method that find the 5 most common lottery numbers otos.csv
import csv

csv_file = open('otos.csv', 'r')
content = csv.reader(csv_file, delimiter=';')
new_list = []

def five_most_frequented_number():
    for row in content:
        new_list.append(row)
    return new_list


print(five_most_frequented_number())
