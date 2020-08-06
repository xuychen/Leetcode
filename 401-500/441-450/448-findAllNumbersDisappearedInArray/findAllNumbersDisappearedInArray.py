class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        return [i + 1 for i, num in enumerate(nums) if num != i + 1]

    def findDisappearedNumbers2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # For each number i in nums,
        # we mark the number that i points as negative.
        # Then we filter the list, get all the indexes
        # who points to a positive number
        
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]