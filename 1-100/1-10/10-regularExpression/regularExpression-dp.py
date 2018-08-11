# slow version dp

class Solution(object):         
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        sLength, pLength = len(s), len(p)
        matrix = [[False] * (pLength+1) for i in range(sLength+1)]
        matrix[0][0] = True
        
        for i in range(sLength+1):
            for j in range(1, pLength+1):
                matrix[i][j] = matrix[i][j - 2] or (i > 0 and (s[i - 1] == p[j - 2] or p[j - 2] == '.') and matrix[i - 1][j])\
                if p[j - 1] == '*' else i > 0 and matrix[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
        
        return matrix[-1][-1]