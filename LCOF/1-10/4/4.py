class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or not matrix[0]:
            return False

        n_rows = len(matrix)
        n_cols = len(matrix[0])

        i, j = n_rows-1, 0

        while i >= 0 and j < n_cols:
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
            else:
                return True

        return False
