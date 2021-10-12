class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        return int(((8 * n + 1) ** 0.5 - 1) / 2)

    def arrangeCoins2(self, n):
        """
        :type n: int
        :rtype: int
        """

        return int((1 + n << 3) ** 0.5 - 1) >> 1