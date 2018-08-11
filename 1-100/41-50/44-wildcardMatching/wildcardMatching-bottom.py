# dp bottom-up

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        sLength, pLength = len(s), len(p)
        matrix = [[False] * (pLength + 1) for i in range(sLength+1)]
        matrix[0][0] = True
        
        for i in range(sLength+1):
            for j in range(1, pLength+1):
                matrix[i][j] = matrix[i-1][j] or matrix[i][j-1] if p[j-1] == "*" \
                    else i > 0 and p[j-1] in {s[i-1], "?"} and matrix[i-1][j-1]
                    
        return matrix[-1][-1]
                    