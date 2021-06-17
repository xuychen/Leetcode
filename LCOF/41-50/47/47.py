class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n_rows, n_cols = len(grid), len(grid[0])
        dp = [[0] * n_cols for _ in range(n_rows)]
        dp[0][0] = grid[0][0]

        for i in range(1, n_rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n_cols):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, n_rows):
            for j in range(1, n_cols):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[-1][-1]
