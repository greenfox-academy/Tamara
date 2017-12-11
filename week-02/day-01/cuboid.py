# Write a program that stores 3 sides of a cuboid as variables (doubles)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000

a = 10
b = 10
c = 10

def surface_area():
    area = (2 * a * b) + (2 * a * c) + (2 * b * c)
    return "Surface Area: " + str(area)


def volume():
    volume_of_cuboid = a * b * c
    return "Volume: " + str(volume_of_cuboid)


print(surface_area())
print(volume())