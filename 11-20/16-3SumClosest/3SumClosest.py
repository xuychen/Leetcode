class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        length = len(nums)
        if length < 3:
            return 0
        
        nums.sort()
        closest = 1000000
        for i in range(length-2):
            left = i + 1
            right = length-1
            
            while left < right:
                summation = nums[i] + nums[left] + nums[right]
                if summation > target:
                    if summation - target < closest:
                        closest = summation - target
                        result = summation
                    right -= 1
                elif summation < target:
                    if target - summation < closest:
                        closest = target - summation
                        result = summation
                    left += 1
                else:
                    return summation
            
        return result