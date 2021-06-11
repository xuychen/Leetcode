class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(len(nums)):
            index = nums[i]
            if i != index:
                while index != nums[index]:
                    tmp = nums[index]
                    nums[index] = index
                    index = tmp

                return index

        return None