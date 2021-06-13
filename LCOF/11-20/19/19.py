class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        s_length = len(s)
        p_length = len(p)

        dp =  [[False] * (s_length+1) for _ in range(p_length+1)]
        dp[0][0] = True

        for i in range(1, p_length+1):
            for j in range(s_length+1):
                if j and (s[j-1] == p[i-1] or p[i-1] == '.'):
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    dp[i][j] = dp[i-2][j]
                    if j and (s[j-1] == p[i-2] or p[i-2] == '.'):
                        dp[i][j] |= dp[i][j-1]

        return dp[-1][-1]
    