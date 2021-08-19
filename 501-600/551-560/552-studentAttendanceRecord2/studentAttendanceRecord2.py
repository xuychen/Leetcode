class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1
        MOD = 10**9 + 7

        for _ in range(n):
            new_dp = [[0] * 3 for _ in range(2)]
            for a in range(2):
                for l in range(3):
                    if a < 1:
                        new_dp[a+1][0] = (new_dp[a+1][0] + dp[a][l]) % MOD
                    if l < 2:
                        new_dp[a][l+1] = (new_dp[a][l+1] + dp[a][l]) % MOD

                    new_dp[a][0] = (new_dp[a][0] + dp[a][l]) % MOD

            dp = new_dp

        return sum(map(sum, dp)) % MOD