# Write a program that asks for two numbers
# Thw first number represents the number of girls that comes to a party, the
# second the boys
# It should print: The party is exellent!
# If the the number of girls and boys are equal and there are more people coming than 20
#
# It should print: Quite cool party!
# It there are more than 20 people coming but the girl - boy ratio is not 1-1
#
# It should print: Average party...
# If there are less people coming than 20
#
# It should print: Sausage party
# If no girls are coming, regardless the count of the people

girls = input("How many girls go to the party? ")
boys = input("How many boys go to the party? ")
x = int(girls)
y = int(boys)
if x == 0:
    print("Sausage party")
else:
    if (x + y) >= 20:
        if x == y:
            print("The party is excellent")
        elif x > 0: 
            print("Quite cool party!")
    elif (x + y) < 20:
        print("Average party..")