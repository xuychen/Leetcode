import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return 0

        primes = [True] * (n - 1)
        primes[0] = False

        for i in range(2, int(n ** 0.5)+1):
            if primes[i - 1]:
                primes[i ** 2 - 1: n - 1: i] = [False] * int(math.ceil(float(n - i ** 2) / i))

        return sum(primes)