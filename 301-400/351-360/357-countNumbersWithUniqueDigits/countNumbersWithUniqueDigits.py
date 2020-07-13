class Solution(object):
    def nPr(self, n, k):
        return reduce(lambda a, b: a * b, range(n-k+1, n+1), 1)

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        return sum(self.nPr(9, i) for i in range(n)) * 9 + 1