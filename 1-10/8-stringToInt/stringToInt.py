class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        ASCII0 = 48
        INT_MAX = 2147483647
        minus = False
        start = 0
        end = -1
        result = 0
        length = len(str)
        
        while start < length and str[start] == ' ':
            start += 1
        
        if start >= length:
            return 0
        elif str[start] == '-':
            start += 1
            minus = True
        elif str[start] == '+':
            start += 1
        elif not str[start].isnumeric():
            return 0
        
        end = start
        while end < len(str) and str[end].isnumeric():
            end += 1
            
        if end == start:
            return 0
            
        for i in range(end-start):
            digit = ord(str[end-i-1]) - ASCII0
            result += digit * 10 ** i
              
        if minus == True:
            if result > INT_MAX + 1:
                result = INT_MAX + 1
            result = -result
        else:
            if result > INT_MAX:
                result = INT_MAX
        
        return result