class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        length = len(nums)
        diff = (1 + length) * length / 2 - sum(nums)

        for i, num in enumerate(nums):
            if i != num - 1:
                while nums[i] != nums[num-1]:
                    nums[i], nums[num-1] = nums[num-1], nums[i]
                    num = nums[i]

                if i != num - 1:
                    return [nums[i], nums[i]+diff]

        return []