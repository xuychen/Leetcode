class Solution(object):
    def count(self, matrix, n_rows, n_cols, num):
        x, y = n_rows - 1, 0
        result = 0

        while x >= 0:
            if y < n_cols and matrix[x][y] <= num:
                y += 1
            else:
                result += y
                x -= 1

        return result

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        n_rows = len(matrix)
        n_cols = len(matrix[0])

        left, right = matrix[0][0], matrix[n_rows-1][n_cols-1]
        while left < right:
            mid = left + (right - left) / 2
            if (self.count(matrix, n_rows, n_cols, mid) < k):
                left = mid + 1
            else:
                right = mid

        return left