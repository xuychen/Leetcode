class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        result = 1
        if n < 0:
            n = -n
            x = 1 / x

        while n > 0:
            if n & 1:
                result *= x

            x **= 2
            n >>= 1

        return result