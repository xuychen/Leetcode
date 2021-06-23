class Solution(object):
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """

        return n and (self.sumNums(n-1) + n)