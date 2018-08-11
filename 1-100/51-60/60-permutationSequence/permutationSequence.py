class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        result = ""
        k -= 1
        options = [str(i) for i in range(1, n+1)]
        factorials = self.factorial(n)
        
        for i in range(n-1, -1, -1):
            fact = factorials[i]
            quotient = k / fact
            k -= quotient * fact
            result += options[quotient]
            del options[quotient]
        
        return result
            
        
    def factorial(self, n):
        result = [1]
        fact = 1
        for i in range(1, n):
            fact *= i
            result.append(fact)
            
        return result