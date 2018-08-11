# fast and concise and elegant DP solution

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        length = len(s)
        longest = [0 for i in range(length)]
        res = 0
        
        for i in range(1, length):
            char = s[i]
            parLength = longest[i-1]
            if char == ")" and i - parLength - 1 >= 0 and s[i-parLength-1] == "(":
                longest[i] = longest[i-parLength-2] + parLength + 2
                res = res if res > longest[i] else longest[i]

        return res