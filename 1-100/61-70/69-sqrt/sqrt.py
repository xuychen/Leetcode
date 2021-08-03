class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if not x:
            return x

        original = x
        nextx = (x + original / x) / 2.0
        while x - nextx > 0.000001:
            x = nextx
            nextx = (x + original / x) / 2.0

        return int(nextx)