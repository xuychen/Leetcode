class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        diff = m & n
        changed_bit = n ^ diff

        num = 1
        while changed_bit > num:
            num <<= 1
            
        return 2147483647 - num + 1 & diff
