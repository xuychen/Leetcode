import bisect

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or not matrix[0]:
            return False

        xs, xe, ys, ye = 0, len(matrix), 0, len(matrix[0])
        while True:
            row_s, col_s = map(lambda line: line[ys], matrix), matrix[xs]

            row_s_index = bisect.bisect_left(row_s, target, xs, xe)
            if row_s_index != xe and row_s[row_s_index] == target:
                return True
            else:
                xe = row_s_index

            col_s_index = bisect.bisect_left(col_s, target, ys, ye)
            if col_s_index != ye and col_s[col_s_index] == target:
                return True
            else:
                ye = col_s_index

            if xe <= xs + 1 or ye <= ys + 1:
                return False

            row_e, col_e = map(lambda line: line[ye-1], matrix), matrix[xe-1]
            row_e_index = bisect.bisect_left(row_e, target, xs, xe)
            if row_e_index != xe and row_e[row_e_index] == target:
                return True
            else:
                xs = row_e_index

            col_e_index = bisect.bisect_left(col_e, target, ys, ye)
            if col_e_index != ye and col_e[col_e_index] == target:
                return True
            else:
                ys = col_e_index

            if xe <= xs + 1 or ye <= ys + 1:
                return False

    def searchMatrix2(self, matrix, target):
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
