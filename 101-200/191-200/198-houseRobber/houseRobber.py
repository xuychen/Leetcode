class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        dp = [0] * (length+1)
        dp[1] = nums[0]

        for i in range(1, length):
            dp[i+1] = max(dp[i-1]+nums[i], dp[i])

        return dp[-1]