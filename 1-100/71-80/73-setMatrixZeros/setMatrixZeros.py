class Solution(object):
    def __init__(self):
        self.matrix = None
        self.xLength = 0
        self.yLength = 0
        
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        self.matrix = matrix
        self.xLength = len(matrix)
        self.yLength = self.xLength and len(matrix[0])
        
        for i in range(self.xLength):
            for j in range(self.yLength):
                if self.matrix[i][j] == 0:
                    self.spread(i, j)
        
        for i in range(self.xLength):
            for j in range(self.yLength):
                if self.matrix[i][j] == "*":
                    self.matrix[i][j] = 0
        
    def spread(self, x, y):
        for i in range(self.xLength):
            self.matrix[i][y] = "*" if self.matrix[i][y] != 0 else 0
        for i in range(self.yLength):
            self.matrix[x][i] = "*" if self.matrix[x][i] != 0 else 0