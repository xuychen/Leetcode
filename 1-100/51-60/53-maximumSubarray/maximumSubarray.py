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

    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maximum = nums[0]
        summation = 0

        for end in range(len(nums)):
            summation += nums[end]
            maximum = max(maximum, summation)
            if summation < 0:
                summation = 0

        return maximum