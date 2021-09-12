from collections import Counter

def uniquePairs(nums, target):
    counter = Counter(nums)
    count = 0
    for num in counter.keys():
        if 2 * num == target:
            count += counter[num] > 1
        elif num * 2 < target:
            count += counter[target-num] > 0

    return count

nums1 = [1, 1, 2, 45, 46, 46]
target1 = 47
nums2 = [1, 1]
target2 = 2
nums3 = [1, 5, 1, 5]
target3 = 6

print(uniquePairs(nums1, target1)) # 2
print(uniquePairs(nums2, target2)) # 1
print(uniquePairs(nums3, target3)) # 1