class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        self.array, self.length = range(1, n+1), n
        return self.combineHelper(0, k)
        
    def combineHelper(self, start, k):
        if k == 0:
            return [[]]
        
        result = []
        for i in range(start, self.length):
            for each in self.combineHelper(i+1, k-1):
                result.append([self.array[i]] + each)
                
        return result