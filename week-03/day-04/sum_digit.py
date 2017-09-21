# Given a non-negative int n, return the sum of its digits recursively (no loops). 
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while 
# divide (/) by 10 removes the rightmost digit (126 // 10 is 12).

def sum_digit(n):
    print(n)
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digit(n // 10)


print(sum_digit(126))