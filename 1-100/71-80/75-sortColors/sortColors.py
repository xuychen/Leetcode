class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        self.nums = nums
        left, right = 0, len(nums) - 1
        i = 0
        
        while i <= right:
            while i <= right:
                num = nums[i]
                if num == 0:
                    self.swap(left, i)
                    left += 1
                elif num == 2:
                    self.swap(i, right)
                    right -= 1
                else:
                    break
                    
                i = max(left, i)
            i += 1
                
    def swap(self, left, right):
        tmp = self.nums[right]
        self.nums[right] = self.nums[left]
        self.nums[left] = tmp