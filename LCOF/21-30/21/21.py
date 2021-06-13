class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        odds, evens = [], []
        for num in nums:
            if num & 1:
                odds.append(num)
            else:
                evens.append(num)

        return odds + evens

    def exchange2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] & 1:
                left += 1
            elif nums[right] & 1 == 0:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]

        return nums