def isHappy(n):
    seen = set()

    while n != 1:
        if n in seen:
            return False
        seen.add(n)

        n = sum(int(digit) ** 2 for digit in str(n))

    return True

n = 19

if isHappy(n):
    print('Happy number')
else:
    print('Not happy')