class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        start, end = 0, len(nums)

        for elem in nums:
            if elem:
                nums[start] = elem
                start += 1

        for i in range(start, end):
            nums[i] = 0