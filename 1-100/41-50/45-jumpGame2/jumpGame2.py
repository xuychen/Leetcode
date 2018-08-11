class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        length = len(nums)
        i = times = startIndex = 0
        
        while i < length - 1:
            num = nums[i] or 1
            if i + num >= length - 1:
                return times + 1
            
            maximum = 0
            for j in range(startIndex + 1, i + num + 1):
                if maximum <= j + nums[j]:
                    maximum = j + nums[j]
                    maxIndex = j
                    
            times += 1
            startIndex = i + num
            i = maxIndex
                        
        return times