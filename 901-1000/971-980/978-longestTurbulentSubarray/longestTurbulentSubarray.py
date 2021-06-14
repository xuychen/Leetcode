class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        result = 1
        start = 0
        high = True

        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]:
                start = i
            elif high ^ (arr[i-1] > arr[i]):
                start = i - 1
            else:
                high = not high

            result = max(i - start + 1, result)

        return result