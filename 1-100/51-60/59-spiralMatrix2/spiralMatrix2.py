class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        matrix = [[0] * n for i in range(n)]
        i = j = 0
        number = 1
        
        for loop in range((n+1) / 2):
            for j in range(loop, n-loop):
                matrix[i][j] = number
                number += 1
            for i in range(loop+1, n-loop):
                matrix[i][j] = number
                number += 1
            for j in range(n-loop-2, loop-1, -1):
                matrix[i][j] = number
                number += 1
            for i in range(n-loop-2, loop, -1):
                matrix[i][j] = number
                number += 1
        
        return matrix