class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        length = len(s)
        size = [0 for i in range(length)]
        stack = [0 for i in range(length)]
        stackPtr = 0
        summing = 0
        res = 0
        
        for i, char in enumerate(s):
            if char == "(":
                stack[stackPtr] = i
                stackPtr += 1
            elif char == ")":
                if stackPtr > 0:
                    prev = stack[stackPtr-1]
                    diff = i - stack[stackPtr-1] + 1
                    size[prev] = diff
                    stackPtr -= 1
        
        i = 0
        while i < length:
            parLength = size[i]
            if parLength != 0:
                summing += parLength
                i += parLength
            else:
                res = res if summing < res else summing
                summing = 0
                i += 1
        
        res = res if summing < res else summing
        return res