# - Create an array variable named `ag`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Double all the values in the array

ag = [3, 4, 5, 6, 7]
print(ag[0:5] * 2)


ag = [3, 4, 5, 6, 7]
def double_ag(doubles):
    for i in range(len(doubles)):
        doubles[i] *= 2
    return doubles
print(double_ag(ag))