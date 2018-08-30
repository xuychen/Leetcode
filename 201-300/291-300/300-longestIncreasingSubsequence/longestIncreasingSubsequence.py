import bisect
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        targetArray, length = [], 0
        
        for num in nums:
            index = bisect.bisect_left(targetArray, num, 0, length)
            if index == length:
                targetArray.append(num)
                length += 1
            else:
                targetArray[index] = num
                
        return length