class Solution(object):
    def get_primes(self):
        primes = [2,3,5,7]
        for num in range(7, 1001, 2):
            prime_flag = True
            for prime in primes:
                if num % prime == 0:
                    prime_flag = False
                    break

            if prime_flag:
                primes.append(num)

        return primes

    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """

        result = 0
        primes = self.get_primes()
        index = 0

        while n > 1:
            if n % primes[index] == 0:
                n /= primes[index]
                result += primes[index]
            else:
                index += 1

        return result