class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums = set(nums)
        best = 0
        for num in nums:
            if num - 1 not in nums:
                y = num + 1
                while y in nums:
                    y += 1
                
                best = max(best, y-num)
    
        return best