class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        result = [1] if rowIndex >= 0 else []
        for row in range(1, rowIndex+1):
            for i in range(row-1, 0, -1):
                result[i] += result[i-1]
            result.append(1)
        return result