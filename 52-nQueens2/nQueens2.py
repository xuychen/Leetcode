class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        return self.nQueensHelper([-1] * n, 0)
        
    def nQueensHelper(self, array, count):
        length = len(array)
        if count == length:
            return 1
        
        result = 0
        for i in range(length):
            flag = True
            for j in range(count):
                if i == array[j] or array[j] - j + count == i or array[j] + j - count == i:
                    flag = False
                    break
                    
            if flag:
                array[count] = i
                result += self.nQueensHelper(array, count+1)
        
        return result