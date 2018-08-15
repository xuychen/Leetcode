# top down dp solution

class Solution(object):
    def __init__ (self):
        self.matrix = {}
        self.word1 = ""
        self.word2 = ""
        
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        self.word1, self.word2 = word1, word2
        length1, length2 = len(word1), len(word2)
        
        for i in range(0, length1+1):
            self.matrix[i, 0] = i
        for i in range(1, length2+1):
            self.matrix[0, i] = i
        
        return self.minDistanceRecursion(length1, length2)
        
    def minDistanceRecursion(self, i, j):
        if self.matrix.get((i,j), -1) != -1:
            return self.matrix[i, j]
        
        self.matrix[i, j] = min(self.minDistanceRecursion(i-1, j), self.minDistanceRecursion(i, j-1),
                           self.minDistanceRecursion(i-1, j-1)) + 1 if self.word1[i-1] != self.word2[j-1] \
                            else self.minDistanceRecursion(i-1, j-1)
            
        return self.matrix[i, j]   