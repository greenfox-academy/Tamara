# Write a program that asks for an integer that is a distance in kilometers,
# then it converts that value to miles and prints it

km_to_mile = 0.6214
distance = input("distance in km ")
mile = km_to_mile * float(distance)

print(str(mile) + " mile")