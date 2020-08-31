class Solution(object):
    def __init__(self):
        self.dp = {}

    def findTargetSumWays(self, nums, S, index=0):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        if index == len(nums):
            return not S
        if (S, index) not in self.dp:
            self.dp[(S, index)] = sum([self.findTargetSumWays(nums, S + sign * nums[index], index + 1) for sign in (1, -1)])

        return self.dp[(S, index)]