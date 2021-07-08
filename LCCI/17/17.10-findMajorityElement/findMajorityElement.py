class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        main = nums[0]
        count = 0

        for num in nums:
            if count == 0:
                main = num

            if num == main:
                count += 1
            else:
                count -= 1

        return main if nums.count(main) > len(nums) / 2 else -1