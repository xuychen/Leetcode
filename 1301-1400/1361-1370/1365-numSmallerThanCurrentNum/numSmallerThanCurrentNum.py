class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        length = len(nums)
        new_nums = sorted(zip(nums, range(length)))

        prev = -1
        result = [0] * length

        for i in range(length):
            if prev == -1 or new_nums[i][0] != new_nums[i - 1][0]:
                prev = i

            result[new_nums[i][1]] = prev

        return result