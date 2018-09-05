import copy

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        row = copy.deepcopy(triangle[-1])
        for level in range(len(triangle)-2, -1, -1):
            for i in range(level+1):
                row[i] = triangle[level][i] + min(row[i], row[i+1])
        return row[0]