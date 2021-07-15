class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        prev = 0
        for num in sorted(arr):
            if num > prev:
                prev += 1

        return prev