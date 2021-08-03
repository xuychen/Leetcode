class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        maximums = nums[:]
        minimums = nums[:]
        left, right = 0, length - 1

        for i in range(1, length):
            maximums[i] = max(maximums[i-1], nums[i])
        for i in range(length-2, -1, -1):
            minimums[i] = min(minimums[i+1], nums[i])

        for i in range(length):
            if minimums[i] == maximums[i]:
                left = i + 1
            else:
                break

        for i in range(length-1, left, -1):
            if minimums[i] == maximums[i]:
                right = i - 1
            else:
                break

        return right - left + 1
