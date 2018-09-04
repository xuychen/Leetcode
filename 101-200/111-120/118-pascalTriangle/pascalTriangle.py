class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        result = [[1]] if numRows else []
        for row in range(1, numRows):
            prev, array = result[row-1], [1]
            for i in range(1, row):
                array.append(prev[i-1]+prev[i])
            result.append(array+[1])
        return result