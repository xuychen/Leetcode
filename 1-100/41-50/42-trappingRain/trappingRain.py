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

    def trap2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        length = len(height)
        maximum = 0
        result = []

        for i in range(length):
            maximum = max(maximum, height[i])
            result.append(maximum - height[i])

        maximum = 0
        for i in range(length-1, -1, -1):
            maximum = max(maximum, height[i])
            result[i] = min(result[i], maximum - height[i])

        return sum(result)