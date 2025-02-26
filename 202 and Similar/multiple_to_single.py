# Given a positive integer n, repeatedly replace n with the product of its digits until it becomes 
# a single-digit number. Return the number of 
# steps it takes to reach a single-digit number.

import math

def multiple_to_single(n):
    steps = 0
    while n > 9:
        n = math.prod(int(digit) for digit in str(n))
        steps += 1
    return steps

n = 999  
print('Total steps to become a single digit: ', multiple_to_single(n))
print('Total steps to become a single digit: ', multiple_to_single(39))
print('Total steps to become a single digit: ', multiple_to_single(5))