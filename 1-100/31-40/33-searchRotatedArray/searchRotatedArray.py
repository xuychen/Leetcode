class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (right + left) // 2
            if nums[mid] < target:
                if nums[right] >= target or (nums[left] < target and nums[mid] > nums[left]):
                    left = mid + 1
                else:
                    right = mid    
            elif nums[mid] > target:
                if nums[left] <= target or (nums[left] > target and nums[mid] < nums[left]):
                    right = mid
                else:
                    left = mid + 1
            else:
                return mid
            
        return left if nums[left: left+1] == [target] else -1