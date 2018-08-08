class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        xLength = len(matrix)
        yLength = xLength and len(matrix[0])
        times = min(xLength+1, yLength+1)
        i = j = 0
        result = []
        
        for loop in range(times / 2):
            result += [matrix[i][j] for j in range(loop, yLength-loop)] + [matrix[i][j] for i in range(loop+1, xLength-loop)]
            if loop * 2 != times - 2:
                result += [matrix[i][j] for j in range(yLength-loop-2, loop-1, -1)] + [matrix[i][j] for i in range(xLength-loop-2, loop, -1)]
        
        return result