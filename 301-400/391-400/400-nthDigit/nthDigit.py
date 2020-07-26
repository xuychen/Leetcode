class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """

        for digits in range(1, 11):
            if n <= digits * 9 * 10 ** (digits-1):
                quotient = (n - 1) / digits
                remainder = (n - 1) % digits
                return (10 ** (digits-1) + quotient) / 10 ** (digits - remainder - 1) % 10

            n -= digits * 9 * 10 ** (digits-1)