class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stackPtr = 0
        length = len(s)
        stack = [""] * (length / 2 + 1)
        dic = {"}": "{", ")": "(", "]": "["}
        
        for i, char in enumerate(s):
            if stackPtr >= length / 2 + 1:
                return False
            elif char in ["{", "(", "["]:
                stack[stackPtr] = char
                stackPtr += 1
            elif char in ["}", ")", "]"] and stackPtr > 0 and dic[char] == stack[stackPtr-1]:
                stackPtr -= 1
            else:
                return False
            
        return True if stackPtr == 0 else False
                
                