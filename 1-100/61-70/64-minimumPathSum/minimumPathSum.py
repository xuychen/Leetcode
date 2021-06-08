import copy

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        matrix = copy.deepcopy(grid)
        xLength = len(grid)
        yLength = xLength and len(grid[0])

        for i in range(1, xLength):
            matrix[i][0] += matrix[i-1][0]
        for i in range(1, yLength):
            matrix[0][i] += matrix[0][i-1]

        for i in range(1, xLength):
            for j in range(1, yLength):
                matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])

        return matrix[-1][-1]

    def minPathSum2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid:
            return 0
        if not grid[0]:
            return 0

        sum_grid = []
        n_rows, n_cols = len(grid), len(grid[0])
        sum_grid.append(grid[0][0])
        for j in range(1, n_cols):
            sum_grid.append(sum_grid[-1]+grid[0][j])

        for i in range(1, n_rows):
            sum_grid[0] += grid[i][0]
            for j in range(1, n_cols):
                sum_grid[j] = min(sum_grid[j], sum_grid[j-1]) + grid[i][j]

        return sum_grid[-1]