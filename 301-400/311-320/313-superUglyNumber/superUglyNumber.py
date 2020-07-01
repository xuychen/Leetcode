class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        length = len(primes)
        counter = [0] * length
        listing = [1]
        size = 1

        while size < n:
            minimum = min([listing[counter[i]] * primes[i] for i in range(length)])
            for i, prime in enumerate(primes):
                if not minimum % prime:
                    counter[i] += 1

            listing.append(minimum)
            size += 1

        return listing[-1]
                