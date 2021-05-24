# dp bottom-up

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        sLength, pLength = len(s), len(p)
        matrix = [[False] * (pLength + 1) for i in range(sLength+1)]
        matrix[0][0] = True

        for i in range(sLength+1):
            for j in range(1, pLength+1):
                matrix[i][j] = matrix[i-1][j] or matrix[i][j-1] if p[j-1] == "*" \
                    else i > 0 and p[j-1] in {s[i-1], "?"} and matrix[i-1][j-1]

        return matrix[-1][-1]

    # my own version
    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        s_length = len(s)
        p_length = len(p)
        dp = [[False for _ in range(p_length+1)] for _ in range(s_length+1)]
        dp[0][0] = True

        for i in range(1, p_length+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-1]

        for i in range(1, s_length+1):
            for j in range(1, p_length+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] |= dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] |= dp[i][j-1] or dp[i-1][j]

        return dp[-1][-1]

    # p_length space complexity
    def isMatch3(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        s_length = len(s)
        p_length = len(p)
        dp = [False] * (p_length+1)
        dp[0] = True

        for i in range(1, p_length+1):
            if p[i-1] == '*':
                dp[i] = dp[i-1]

        for i in range(1, s_length+1):
            dp2 = [False] * (p_length+1)
            for j in range(1, p_length+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp2[j] |= dp[j-1]
                elif p[j-1] == '*':
                    dp2[j] |= dp2[j-1] or dp[j]

            dp = dp2

        return dp[-1]