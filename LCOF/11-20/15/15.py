class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        return "{0:b}".format(n).count('1')