def isCovered(ranges, left, right):
    covered = set()
    
    for start, end in ranges:
        for num in range(start, end+1):
            covered.add(num)
    return all(num in covered for num in range(left, right+1))
    
ranges = [[1,10],[10,20]]
left = 21
right = 21

print(isCovered(ranges, left, right))