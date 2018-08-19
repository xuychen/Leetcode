class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) / 2
            
            if target == nums[mid]:
                return True
            elif nums[left] == nums[mid]:
                if nums[left] == nums[0]:
                    return self.search(nums[left: mid+1], target) or self.search(nums[mid+1:], target)
                else:
                    left = mid + 1
            elif nums[left] > nums[mid] and nums[left] >= nums[0]:
                if target >= nums[left]:
                    if target < nums[mid] or nums[left] > nums[mid]:
                        right = mid
                    else:
                        left = mid + 1
                else:
                    if target < nums[mid]:
                        right = mid
                    else:
                        left = mid + 1
            else:
                if target >= nums[left] and target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
                    
        return nums != [] and nums[left] == target