class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix or not matrix[0]:
            return []

        n_rows, n_cols = len(matrix), len(matrix[0])
        result = []
        step = -1

        for step in range((min(n_cols, n_rows)+1)/2):
            for i in range(step, n_cols-step):
                result.append(matrix[step][i])
            for i in range(step+1, n_rows-step-1):
                result.append(matrix[i][n_cols-step-1])
            if step != n_rows-step-1:
                for i in range(n_cols-step-1, step-1, -1):
                    result.append(matrix[n_rows-step-1][i])
            if step != n_cols-step-1:
                for i in range(n_rows-step-2, step, -1):
                    result.append(matrix[i][step])

        return result