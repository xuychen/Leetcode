class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        length = len(nums)
        sorted_nums = sorted(nums)
        count = 0
        start = 0
        result = 1

        for i in range(1, length):
            num = sorted_nums[i]
            count += (num - sorted_nums[i-1]) * (i - start)
            while count > k:
                count -= (num - sorted_nums[start])
                start += 1

            result = max(result, i - start + 1)

        return result