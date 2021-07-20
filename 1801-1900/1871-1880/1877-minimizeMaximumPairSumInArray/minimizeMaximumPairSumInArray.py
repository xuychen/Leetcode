class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left, right = 0, len(nums) - 1
        sorted_nums = sorted(nums)
        result = 0

        while left < right:
            result = max(result, sorted_nums[left] + sorted_nums[right])
            left += 1
            right -= 1

        return result