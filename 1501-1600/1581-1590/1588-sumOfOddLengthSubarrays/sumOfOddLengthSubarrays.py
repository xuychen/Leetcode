class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        length = len(arr)
        prefix = [0] * (length+1)
        result = 0

        for i in range(length):
            prefix[i+1] = prefix[i] + arr[i]

        left, right = 0, length
        currs = []
        curr = 0

        while left <= right:
            curr += prefix[right] - prefix[left]
            currs.append(curr)
            if left & 1 == 0:
                result += curr

            left += 1
            right -= 1

        left += 1 + (left & 1)
        while left <= length:
            result += currs[length-left]
            left += 2

        return result
