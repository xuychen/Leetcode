# top down, need improvement

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
        self.dp = {(0,0): True}
        length1, length2, length3 = len(s1), len(s2), len(s3)
        return self.dp.get((length1, length2), False) or self.isInterleaveHelper(s1, s2, s3, length1, length2) if length1 + length2 == length3 else False
        
    def isInterleaveHelper(self, s1, s2, s3, i, j):
        if i and s1[i-1] == s3[i+j-1] and self.dp.setdefault((i-1, j), self.isInterleaveHelper(s1, s2, s3, i-1, j)):
            return True
        elif j and s2[j-1] == s3[i+j-1] and self.dp.setdefault((i, j-1), self.isInterleaveHelper(s1, s2, s3, i, j-1)):
            return True
        
        return False
