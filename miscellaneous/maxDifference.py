def maxDifference(array):
    minimum, res = 10000, -1

    for num in array:
        if num < minimum:
            minimum = num
        else:
            diff = num - minimum
            res = diff if diff > res else res
    
    return res

import random
arr = random.sample(range(1, 200), 30)

print arr
print maxDifference(arr)