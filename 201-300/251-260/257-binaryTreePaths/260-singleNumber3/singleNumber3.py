class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        answer = group1 = group2 = 0
        for num in nums:
            answer ^= num
            
        i = 0
        while not answer & 1 << i:
            i += 1
            
        pos = 1 << i
        for num in nums:
            if num & pos:
                group1 ^= num
            else:
                group2 ^= num
        
        return [group1, group2]