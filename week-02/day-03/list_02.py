# Join the two lists by matching one girl with one boy in the order list
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ["Eve", "Ashley", "Bözsi", "Kat", "Jane"]
boys = ["Joe", "Fred", "Béla", "Todd", "Neef", "Jeff"]
order = []

for i in range(0, len(girls)):
    order += ([girls[i]] + [boys[i]])

#girls.extend(boys)
#order.extend(girls)


print(order)
