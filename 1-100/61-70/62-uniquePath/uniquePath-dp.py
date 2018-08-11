class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        if not m or not n:
            return 0
        
        matrix = [[1] * n] + [[1] + [0] * (n - 1) for i in range(m-1)]
        
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
                
        return matrix[-1][-1]