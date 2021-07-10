class Solution(object):
    def check_peak(self, nums, i, length):
        left = right = True
        if i < length - 1:
            right = nums[i] > nums[i+1]
        if i > 0:
            left = nums[i] > nums[i-1]

        return left * 2 + right

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        left, right = 0, length - 1

        while left <= right:
            mid = left + (right - left) / 2
            peak = self.check_peak(nums, mid, length)
            if peak == 3:
                return mid
            elif peak == 2:
                left = mid + 1
            else:
                right = mid - 1

        return -1
