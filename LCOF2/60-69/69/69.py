class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        index = 0
        maximum = arr[0]

        for i, num in enumerate(arr):
            if num > maximum:
                maximum = num
                index = i

        return index