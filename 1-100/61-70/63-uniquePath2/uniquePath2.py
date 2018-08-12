class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        xLength = len(obstacleGrid)
        yLength = xLength and len(obstacleGrid[0])
        
        if not xLength or not yLength:
            return 0
        
        matrix = [[0] * yLength for i in range(xLength)]
        matrix[0][0] = 0 if obstacleGrid[0][0] else 1
            
        for i in range(xLength):
            for j in range(yLength):
                if obstacleGrid[i][j] != 1:
                    up = matrix[i-1][j] if i else 0
                    left = matrix[i][j-1] if j else 0
                    matrix[i][j] += up + left
                
        return matrix[-1][-1]