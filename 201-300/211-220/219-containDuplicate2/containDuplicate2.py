class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        dictionary = {}
        for i in range(len(nums)):
            num = nums[i]
            prevIndex = dictionary.get(num, -1)
            if prevIndex != -1 and i - prevIndex <= k:
                return True
            
            dictionary[num] = i
            
        return False