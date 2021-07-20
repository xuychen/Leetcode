class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        MOD = 10 ** 9 + 7
        sorted_nums = sorted(nums)
        left, right = 0, len(sorted_nums) - 1
        result = 0

        while left <= right:
            if sorted_nums[left] + sorted_nums[right] <= target:
                result = (result + (1 << (right - left))) % MOD
                left += 1
            else:
                right -= 1

        return result
