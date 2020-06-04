class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        start = 0
        num = 0
        length = len(nums)
        min_size = length + 1

        for end in range(length):
            num += nums[end]

            if num >= s:
                while num >= s:
                    num -= nums[start]
                    start += 1

                min_size = min(min_size, end - start + 2)

        return min_size if min_size <= length else 0 