# bottom up dp solution

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        length1, length2 = len(word1), len(word2)
        matrix = [[0] * (length2 + 1) for i in range(length1+1)]
        
        for i in range(1, length1+1):
            matrix[i][0] = i
        for i in range(1, length2+1):
            matrix[0][i] = i
        
        for i in range(1, length1+1):
            for j in range(1, length2+1):
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1 \
                if word1[i-1] != word2[j-1] else matrix[i-1][j-1]
            
        return matrix[-1][-1]   