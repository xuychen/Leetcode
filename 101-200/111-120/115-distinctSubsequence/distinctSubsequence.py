# bottom up

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        sLength, tLength = len(s), len(t)
        array = [1] + [0] * tLength
        for i in range(1, sLength+1):
            for j in range(min(i, tLength), 0, -1):
                array[j] += array[j-1] if s[i-1] == t[j-1] else 0
        return array[-1]      