class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        for i, num in enumerate(nums):
            for perm in self.permute(nums[:i] + nums[i+1:]):
                result.append([num] + perm)
            
        return result or [[]]