class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(height) - 1
        maxArea = 0
        
        while left < right:
            lowerHeight =  height[left] if height[left] < height[right] else height[right]
            area = (right-left) * lowerHeight
            maxArea = maxArea if area < maxArea else area
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return maxArea