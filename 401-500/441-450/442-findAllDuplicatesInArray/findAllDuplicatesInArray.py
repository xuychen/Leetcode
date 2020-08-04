class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = []

        for i in range(len(nums)):
            while nums[i] and nums[i] != i + 1:
                if nums[i] == nums[nums[i]-1]:
                    result.append(nums[i])
                    nums[i] = 0
                else:
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        return result

    # good solution from Leetcode
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1

        return res