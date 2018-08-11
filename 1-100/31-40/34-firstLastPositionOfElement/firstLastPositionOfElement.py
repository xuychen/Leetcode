class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left, right = 0, len(nums)
        
        # find target first
        while left < right:
            mid = (left + right) / 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                start, end = self.searchBounds(nums, target, left, mid), self.searchBounds(nums, target+1, mid, right) - 1
                return [start, end]
                
        return [-1, -1]
    
    def searchBounds(self, nums, target, left, right):
        while left < right:
            mid = (left + right) / 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left