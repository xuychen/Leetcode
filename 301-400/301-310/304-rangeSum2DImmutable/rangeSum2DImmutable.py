class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """

        self.matrix = [[0] * ((len(matrix[0]) if matrix else 0) + 1)]

        for line in matrix:
            prev = self.matrix[-1]
            nums = [0]
            left_sum = 0
            for i in range(len(line)):
                nums.append(line[i] + left_sum + prev[i+1])
                left_sum += line[i]

            self.matrix.append(nums)


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        return self.matrix[row2+1][col2+1] - self.matrix[row2+1][col1] - self.matrix[row1][col2+1] + self.matrix[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)