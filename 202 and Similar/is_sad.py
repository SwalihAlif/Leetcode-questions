def is_sad(n):

    seen = set()

    while n != 1:
        if n in seen:
            return True
        seen.add(n)

        n = sum(int(digit) ** 2 for digit in str(n))

    return False

n = 123
if is_sad(n):
    print('Sad number')
else:
    print('Not sad')