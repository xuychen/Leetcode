class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        power = 1
        while power <= num:
            power <<= 1

        return power - 1 - num

    def findComplement2(self, num):
        """
        :type num: int
        :rtype: int
        """

        n, i = num, 0
        while n > 0:
            i = n
            n -= n & -n

        return ~num & (i - 1)