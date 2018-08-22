class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        length = len(nums)
        k %= length
        
        if k != 0:
            nums.extend(nums[:-k])
            del nums[:length-k]