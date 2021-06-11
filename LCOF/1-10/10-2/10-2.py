class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(n):
            dp[i+1] = int((dp[i] + dp[i+1]) % (1e9+7))
            if i + 2 <= n:
                dp[i+2] = int((dp[i] + dp[i+2]) % (1e9+7))

        return dp[-1]