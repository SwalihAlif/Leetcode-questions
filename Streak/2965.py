from collections import Counter
def findMissingAndRepeatedValues(grid):
    n = len(grid)
    nums = [num for row in grid for num in row]

    needed_sum = n*n*(n*n+1)//2
    actual_sum = sum(nums)

    count = Counter(nums)
    repeated = next(num for num, freq in count.items() if freq == 2)
    print(repeated)

    missing = needed_sum - (actual_sum - repeated)

    return [repeated, missing]
    
grid = [[9,1,7],[8,9,2],[3,4,6]]
print(findMissingAndRepeatedValues(grid))