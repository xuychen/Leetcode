class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return sum(nums) - len(nums) * min(nums)

    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        minimum = nums[0]
        result = 0

        for i in range(len(nums)):
            if nums[i] < minimum:
                result += i * (minimum - nums[i])
                minimum = nums[i]

            result += nums[i] - minimum

        return result