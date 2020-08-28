def addContinuousToTarget(nums, target):
    dp = set()

    for num in nums:
        newdp = set()
        dp.add(0)
        for candidate in dp:
            newdp.add(candidate+num)

        dp = newdp
        if target in dp:
            return True
            
    return False

def addToTarget(nums, target):
    dp = set()
    dp.add(0)

    for num in nums:
        for candidate in dp.copy():
            dp.add(candidate+num)

    return target in dp


nums = [2, 3, 5, 8, 1]
target1 = 16
target2 = 22
target3 = 11

print(addToTarget(nums, target1)) # True
print(addToTarget(nums, target2)) # False
print(addToTarget(nums, target3)) # True

print(addContinuousToTarget(nums, target1)) # True
print(addContinuousToTarget(nums, target2)) # False
print(addContinuousToTarget(nums, target3)) # False
