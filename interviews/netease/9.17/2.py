import sys

n = input()

def search(heights, level):
    prev = float('inf')
    level_flag = False
    flag = True
    count = 1

    for num in heights:
        if num > level:
            level_flag = True
        if prev < num:
            flag = True
        elif prev > num:
            if flag and level_flag:
                count += 1
                flag = False
    
        prev = num
    
    return count


for _ in range(n):
    _, x = map(int, sys.stdin.readline().strip().split())
    heights = map(int, sys.stdin.readline().strip().split())
    level = heights[x-1]
    left = search(heights[x-1::-1], level)
    right = search(heights[x-1:], level)
    print(left + right - 2)
