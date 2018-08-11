class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        length = len(matrix)
        for i in range(length / 2):
            for j in range(i, length - i - 1):
                x, y = i, j
                tmp = matrix[x][y]
                for _ in range(3):
                    matrix[x][y] = matrix[length - 1 - y][x]
                    x, y = length - 1 - y, x
                matrix[x][y] = tmp