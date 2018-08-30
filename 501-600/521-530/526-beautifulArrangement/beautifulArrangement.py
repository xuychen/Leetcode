class Solution(object):
    def countArrangement(self, n):
        """
        :type N: int
        :rtype: int
        """
        
        return len(self.count(self.generateArray(n), 0, range(1, n+1), n, []))
    
    
    def count(self, array, index, visit, length, result):
        if index == length:
            return [result]
        
        res = []
        for candidate in array[index]:
            if visit[candidate-1]:
                visit[candidate-1] = 0
                res += self.count(array, index+1, visit, length, result+[candidate])
                visit[candidate-1] = candidate
        return res
        
    def generateArray(self, n):
        array = []
        for i in range(1, n+1):
            factors = self.getNumOfFactors(i)
            j = 2
            while i * j <= n:
                factors.append(i*j)
                j += 1
            array.append(factors)
        return array
        
    def getNumOfFactors(self, n):
        i = 1
        array = []
        while i * i < n:
            if n % i == 0:
                array += [i, n/i]
            i += 1
        return array + ([i] if i * i == n else [])