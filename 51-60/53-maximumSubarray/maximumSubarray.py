class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        result = local = -2147483647
        for num in nums:
            local = local + num if local > 0 else num 
            result = result if local < result else local
                
        return result