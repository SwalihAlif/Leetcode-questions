#Given a positive integer n, repeatedly replace n with the sum of its digits until it becomes a single-digit number.
#This is similar to the previous problem, but instead of summing squares of digits, you sum the digits themselves.

def return_single(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

n = 12345
print(return_single(n))