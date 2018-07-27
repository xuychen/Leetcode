class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def threeSum():
            """
            :type nums: List[int]
            :type target: int
            :rtype: int
            """

            num = nums[index]
            res = []

            for i in range(index+1, length-2):
                if i != index+1 and nums[i] == nums[i-1]:
                    continue
                    
                left = i + 1
                right = length-1

                while left < right:
                    summation = num + nums[i] + nums[left] + nums[right]
                    if summation > target:
                        while left < right and nums[right-1] == nums[right]:
                            right -= 1
                        right -= 1
                    elif summation < target:
                        while left < right and nums[left+1] == nums[left]:
                            left += 1
                        left += 1
                    else:
                        res.append([num, nums[i], nums[left], nums[right]])
                        while left < right and nums[left+1] == nums[left]:
                            left += 1
                        left += 1

            return res
        
        length = len(nums)
        if length < 4:
            return []
            
        nums.sort()
        res = []
        
        for index in range(length-3):
            if index != 0 and nums[index] == nums[index-1]:
                continue
            res += threeSum()
        
        return res