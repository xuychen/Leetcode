class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        array, length = [0, 1], 2
        if n < 2:
            return array[:n+1]
        
        for step in range(1, n):
            for i in range(length-1, -1, -1):
                array.append(1 << step | array[i])
            length *= 2
            
        return array