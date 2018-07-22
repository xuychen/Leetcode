class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        length = len(heights)
        
        if length == 0:
            return 0
        
        heights += [0] # for case that stack[i] = -1
        vertical = [0] * length
        stack = [-1] + [0] * length # for case that has nothing
        stackIndex = 1
        
        # right
        for i in range(length):
            height = heights[i]
            prevIndex = stack[stackIndex-1]
            prevHeight = heights[prevIndex]
            
            while prevHeight > height:
                stackIndex -= 1
                vertical[prevIndex] = i
                prevIndex = stack[stackIndex-1]
                prevHeight = heights[prevIndex]
            stack[stackIndex] = i
            stackIndex += 1
                   
        while stackIndex > 1:
            prevIndex = stack[stackIndex-1]
            stackIndex -= 1
            vertical[prevIndex] = length
            
        # left
        for i in range(length-1, -1, -1):
            height = heights[i]
            prevIndex = stack[stackIndex-1]
            prevHeight = heights[prevIndex]
            
            while prevHeight > height:
                stackIndex -= 1
                vertical[prevIndex] -= i + 1
                prevIndex = stack[stackIndex-1]
                prevHeight = heights[prevIndex]
            stack[stackIndex] = i
            stackIndex += 1
        
        # calculation
        maxArea = 0
        for i in range(length):
            area = vertical[i] * heights[i]
            maxArea = area if area > maxArea else maxArea
        
        return maxArea