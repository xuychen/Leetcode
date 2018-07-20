class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        flag = False
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                flag = True
                pivot = nums[i]
                for j in range(len(nums)-1, i, -1):
                    if nums[j] > pivot:
                        nums[i] = nums[j]
                        nums[j] = pivot
                        break
        
                nums[i+1:] = nums[:i:-1]
                break
                
        if not flag:
            nums[:] = nums[::-1]