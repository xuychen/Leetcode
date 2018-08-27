# dp bottom up

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
        length1, length2, length3 = len(s1), len(s2), len(s3)
        dp = [[False] * (length2+1) for _ in range(length1+1)]
        
        if length1 + length2 != length3:
            return False
        
        dp[0][0] = True
        for i in range(1, length1+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for i in range(1, length2+1):
            dp[0][i] = dp[0][i-1] and s2[i-1] == s3[i-1]
        
        for i in range(1, length1+1):
            for j in range(1, length2+1):
                dp[i][j] = (s1[i-1] == s3[i+j-1] and dp[i-1][j]) or (s2[j-1] == s3[i+j-1] and dp[i][j-1])
        
        return dp[-1][-1]