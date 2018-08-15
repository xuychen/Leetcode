class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        xLength = len(matrix)
        yLength = xLength and len(matrix[0])
        
        if yLength == 0:
            return False
        
        left, right = 0, xLength
        
        while left < right:
            mid = (left + right) / 2
            if matrix[mid][0] < target:
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid
            else:
                return True
        x, left, right = left - 1, 0, yLength 
        
        while left < right:
            mid = (left + right) / 2
            if matrix[x][mid] < target:
                left = mid + 1
            elif matrix[x][mid] > target:
                right = mid
            else:
                return True
        
        return False