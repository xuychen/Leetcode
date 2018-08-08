class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        startCounting = False
        count = 0
        
        for i in range(len(nums)-2, -1, -1):
            if startCounting == True:
                count += 1
                if nums[i] > count:
                    startCounting = False
            elif nums[i] == 0:
                startCounting = True
                count = 0
                
        return not startCounting