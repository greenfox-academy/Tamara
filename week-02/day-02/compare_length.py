# - Create a variable named `p1`
#   with the following content: `[1, 2, 3]`
# - Create a variable named `p2`
#   with the following content: `[4, 5]`
# - Print if `p2` has more elements than `p1`
p1 = [1, 2, 3]
p2 = [4, 5]
def lens (k):     
    i = len(p1)
    j = len(p2) 
    k = j - i
    if  k > 1:
        print(p2[0:])
    elif k < 1:
        p2.append(i)
        k = j - i
        return k
