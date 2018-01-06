# Create a method that find the 5 most common lottery numbers otos.csv
import csv

csv_file = open('otos.csv', 'r')
content = csv.reader(csv_file, delimiter=';')
new_list = []
last_five_slice = slice(-5, None)

def all_lottery_numbers():
    for row in content:
        for num in row[last_five_slice]:
           new_list.append(num)
    return new_list

# def five_most_frequented_number():
#     for 
# print(five_most_frequented_number())

print(all_lottery_numbers())