class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 3:
            return n - 1

        num3 = n / 3
        return (3**num3, 3**(num3-1) * 4, 3 ** num3 * 2)[n % 3]