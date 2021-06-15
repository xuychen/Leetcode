class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + (right - left) / 2
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] > arr[mid]:
                right = mid
            else:
                left = mid + 1

        return None