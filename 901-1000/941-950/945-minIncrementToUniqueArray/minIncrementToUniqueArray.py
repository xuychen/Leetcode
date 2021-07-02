class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        prev = -1
        count = 0
        for num in sorted(nums):
            if num <= prev:
                count += prev + 1 - num
                prev += 1
            else:
                prev = num

        return count