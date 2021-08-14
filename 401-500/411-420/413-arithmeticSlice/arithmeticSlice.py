class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        nums.append(float('inf'))
        difference = float('-inf')
        length = len(nums)
        result = 0

        for i in range(1, length):
            diff = nums[i] - nums[i-1]
            if diff == difference:
                count += 1
            else:
                if count >= 2:
                    result += (count - 1) * count / 2

                difference = diff
                count = 1

        return result