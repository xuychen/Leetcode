class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 1:
            return n

        nums = [0, 1]
        for i in range(2, n+1):
            if i & 1:
                nums.append(nums[i/2] + nums[i/2+1])
            else:
                nums.append(nums[i/2])

        return max(nums)