class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        summation = 0
        result = float('-inf')

        for num in nums:
            summation += num
            result = max(summation, result)
            if summation < 0:
                summation = 0

        return result
