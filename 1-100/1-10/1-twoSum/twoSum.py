class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        length = len(nums)
        hashmap = {}

        for i in range(length):
            if target - nums[i] in hashmap:
                return [hashmap[target-nums[i]], i]
            else:
                hashmap[nums[i]] = i

        return []