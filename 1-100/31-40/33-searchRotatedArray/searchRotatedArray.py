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

    def search2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] < target:
                if nums[right] >= target or (nums[left] < target and nums[mid] > nums[left]):
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] > target:
                if nums[left] <= target or (nums[left] > target and nums[mid] < nums[left]):
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                return mid

        return -1