class Solution(object):
    def trap(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        
        length = len(heights)
        
        if length == 0:
            return 0
        
        stack = [0] * length
        stackIndex = 0
        result = 0
        
        i = 1
        while i < length:
            if stackIndex == 0:
                while i < length and heights[i-1] <= heights[i]:
                    i += 1
                
                if i != length:
                    stack[stackIndex] = i
                    stackIndex = 1
                    level = heights[i]
            else:    
                height = heights[i]
                prevIndex = stack[stackIndex-1]
                prevHeight = heights[prevIndex-1] # the height before that

                if heights[i-1] > height:
                    stack[stackIndex] = i
                    stackIndex += 1
                    level = height
                elif heights[i-1] < height:   
                    while stackIndex > 0 and prevHeight < height:
                        stackIndex -= 1
                        result += (i - prevIndex) * (prevHeight - level)
                        level = prevHeight
                        prevIndex = stack[stackIndex-1]
                        prevHeight = heights[prevIndex-1]

                    if stackIndex > 0 and prevHeight >= height: # current Height is not the highest
                        if prevHeight == height:
                            stackIndex -= 1
                        result += (i - prevIndex) * (height - level)
                        level = height
            i += 1
        
        return result