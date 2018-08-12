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