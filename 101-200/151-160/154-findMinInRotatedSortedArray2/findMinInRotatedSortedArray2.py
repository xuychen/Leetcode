class Solution(object):
    def findMinHelper(self, nums, start, end):
        while start < end:
            mid = (start + end) / 2
            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid
            else:
                return min(self.findMinHelper(nums, start, mid), self.findMinHelper(nums, mid+1, end))

        return nums[start]

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return self.findMinHelper(nums, 0, len(nums) - 1)
