# - Create a variable named `p1`
#   with the following content: `[1, 2, 3]`
# - Create a variable named `p2`
#   with the following content: `[4, 5]`
# - Print if `p2` has more elements than `p1`
p1 = [1, 2, 3]
p2 = [4, 5]
i = len(p1)
j = len(p2) 
k = j - i  
#def lens (k):  
#   while k < 1:
#      p2.append(p1[1])
#      return k
#   else:
#       print(len(k))
#lens(k)

def lens(k):
    if j < i:
       print('less')
    else:
       print('more')
lens(k)