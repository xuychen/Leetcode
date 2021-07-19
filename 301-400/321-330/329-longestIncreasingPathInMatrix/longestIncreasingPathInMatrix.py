import Queue

class Solution(object):
    def dfs(self, matrix, dp, i, j, n_rows, n_cols):
        count = 1

        if dp[i][j] == 0:
            if i > 0:
                if matrix[i][j] > matrix[i-1][j]:
                    count = max(count, self.dfs(matrix, dp, i-1, j, n_rows, n_cols) + 1)
            if j > 0:
                if matrix[i][j] > matrix[i][j-1]:
                    count = max(count, self.dfs(matrix, dp, i, j-1, n_rows, n_cols) + 1)
            if i < n_rows - 1:
                if matrix[i][j] > matrix[i+1][j]:
                    count = max(count, self.dfs(matrix, dp, i+1, j, n_rows, n_cols) + 1)
            if j < n_cols - 1:
                if matrix[i][j] > matrix[i][j+1]:
                    count = max(count, self.dfs(matrix, dp, i, j+1, n_rows, n_cols) + 1)

            dp[i][j] = count
            return count

        return dp[i][j]

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        n_rows, n_cols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
        result = 0

        for i in range(n_rows):
            for j in range(n_cols):
                result = max(result, self.dfs(matrix, dp, i, j, n_rows, n_cols))

        return result
