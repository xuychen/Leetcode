class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2147483647
        if x < 0:
            num = -int(str(-x)[::-1])
            if num >= -INT_MAX:
                return num
            
        else:
            num = int(str(x)[::-1])
            if num <= INT_MAX:
                return num
        
        return 0