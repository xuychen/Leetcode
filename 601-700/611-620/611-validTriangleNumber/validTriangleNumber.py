import bisect

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sorted_nums = sorted(nums)
        length = len(sorted_nums)
        count = 0

        for i in range(length-2):
            for j in range(i+1, length-1):
                count += max(0, bisect.bisect_left(sorted_nums, sorted_nums[i]+sorted_nums[j], j, length) - j - 1)

        return count