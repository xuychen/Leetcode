class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')

        for num in nums:
            if num >= max3:
                max3 = num
            if num >= max2:
                max3 = max2
                max2 = num
            if num >= max1:
                max2 = max1
                max1 = num
            if num <= min2:
                min2 = num
            if num <= min1:
                min2 = min1
                min1 = num

        return max(max1 * max2 * max3, min1 * min2 * max1)