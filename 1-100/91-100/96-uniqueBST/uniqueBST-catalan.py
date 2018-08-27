# using math to get the answer, catalan number

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        return self.choice(2*n, n) / (n+1)
        
    def choice(self, n, k):
        return self.factorial(k+1, n+1) / self.factorial(1, k+1)
        
    def factorial(self, start, end):
        result = 1
        for i in range(start, end):
            result *= i
        return result