class Solution(object):
    def pow(self, n, a):
        result = 1
        while a > 0:
            if a % 2:
                result = int((result * n) % 1000000007)
            n = int((n ** 2) % 1000000007)
            a //= 2
        return result

    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 3:
            return n - 1

        num3 = n / 3
        return int((self.pow(3, num3), self.pow(3, num3-1) * 4, self.pow(3, num3) * 2)[n % 3] % 1000000007)