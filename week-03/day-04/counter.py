# Write a recursive function that takes one parameter: n and counts down from n.

def count_down(num):
    if num <= 1:
        return 1
    else:
        return count_down(num-1)

print(count_down(5))
