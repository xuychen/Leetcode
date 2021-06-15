class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        mode = nums[0]
        count = 0

        for num in nums:
            if num == mode:
                count += 1
            elif count == 0:
                mode = num
                count += 1
            else:
                count -= 1

        return mode