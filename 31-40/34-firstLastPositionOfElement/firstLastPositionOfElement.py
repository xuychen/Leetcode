class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        start = end = -1
        length = len(nums)
        left, right = 0, length
        index = -1
        
        # find target first
        while left < right:
            mid = (left + right) / 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                index = mid
                break
                
        if index != -1:
            start, end = self.searchBounds(nums, target, left, index), self.searchBounds(nums, target+1, index, right)
            if nums[start] != target:
                start += 1
            if end == length or nums[end] != target:
                end -= 1
                
        return [start, end]
    
    def searchBounds(self, nums, target, left, right):
        while left < right:
            mid = (left + right) / 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left