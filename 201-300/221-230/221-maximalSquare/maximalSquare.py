class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix:
            return 0

        dp = map(int, matrix[0])
        maximum = any(dp)

        for i in range(1, len(matrix)):
            prev, dp[0] = dp[0], int(matrix[i][0])
            for j in range(1, len(matrix[0])):
                dp[j], prev = min(dp[j], prev, dp[j-1]) + 1 if matrix[i][j] == '1' else 0, dp[j]

            maximum = max(maximum, max(dp))

        return maximum ** 2