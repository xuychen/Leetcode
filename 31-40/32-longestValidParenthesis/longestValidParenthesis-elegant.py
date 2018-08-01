# this solution is far more elegant, but slower than the normal version I wrote
# I guess it is due to cache miss

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        length = len(s)
        stack = [0 for i in range(length)]
        stackPtr = 0
        total = length
        res = 0
        
        for i, char in enumerate(s):
            if char == "(":
                stack[stackPtr] = i
                stackPtr += 1
            elif char == ")":
                if stackPtr and s[stack[stackPtr-1]] == "(":
                    stackPtr -= 1
                else:
                    stack[stackPtr] = i
                    stackPtr += 1
        
        while stackPtr > 0:
            delimiter = stack[stackPtr-1]
            diff = total - delimiter - 1
            res = diff if res < diff else res
            total = delimiter
            stackPtr -= 1
            
        res = total if res < total else res
        return res