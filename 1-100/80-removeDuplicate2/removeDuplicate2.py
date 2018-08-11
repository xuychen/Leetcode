class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        index = len(nums) - 1
        first = False
        chr = '.' # start point
        
        while index >= 0:
            if chr != nums[index]:
                chr = nums[index]
                first = True
            elif first == True:
                first = False
            else:
                del nums[index]
            index -= 1
            
        return len(nums)
            