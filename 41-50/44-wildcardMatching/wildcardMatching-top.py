class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        sLength, pLength = len(s), len(p)
        memo = {}
            
        def dp(i, j):
            if (i, j) not in memo:
                ans = False
                if j == pLength:
                    ans = i == sLength
                elif i <= sLength:
                    if p[j] == '*':
                        ans = dp(i, j+1) or dp(i+1, j)
                    else:
                        ans = i < sLength and p[j] in {s[i], '?'} and dp(i+1, j+1)
                
                memo[i, j] = ans 
            return memo[i, j]
        
        return dp(0, 0)