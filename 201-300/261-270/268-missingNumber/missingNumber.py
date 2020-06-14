class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        return length * (1 + length) / 2 - sum(nums)