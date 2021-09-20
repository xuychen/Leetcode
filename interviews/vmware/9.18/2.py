import sys
from collections import defaultdict

n, target = map(int, sys.stdin.readline().strip().split())
nums = sorted(map(int, sys.stdin.readline().strip().split()))
visited = 0
count = 0

if target == 0:
    for i, num in enumerate(nums):
        if num == 0:
            count += 1
            visited |= 1 << i

prev_sum_dict = defaultdict(set)
for i, num in enumerate(nums):
    sum_dict = defaultdict(set)
    sum_dict[num].add((1 << i))
    for key, value in prev_sum_dict.items():
        for mask in value:
            sum_dict[key+num].add(mask ^ (1 << i))

    for key, value in sum_dict.items():
        prev_sum_dict[key] |= sum_dict[key]

    print(prev_sum_dict)
    for mask in sum_dict[target]:
        if mask and mask & visited == 0:
            count += 1
            visited |= mask

print(count)
        

