class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        self.nums, self.length = nums, len(nums)
        return [[]] + self.subsetHelper(0)
        
    def subsetHelper(self, start):
        result = []
        for i in range(start, self.length):
            num = self.nums[i]
            if i > start and num == self.nums[i-1]:
                continue
                
            result.append([num])
            for each in self.subsetHelper(i+1):
                result.append([num] + each)
                
        return result