class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.nums, self.length = nums, len(nums)
        return [[]] + self.subsetHelper(0)

    def subsetHelper(self, start):
        result = []
        for i in range(start, self.length):
            result.append([self.nums[i]])
            for each in self.subsetHelper(i+1):
                result.append([self.nums[i]] + each)

        return result

    def subsets2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        length = len(nums)
        result = [[]]

        for i in range(length):
            for rhs in self.subsets(nums[i+1:]):
                result.append([nums[i]] + rhs)

        return result