class Solution(object):
    def consecutiveNumbersSum(self, n):
        """
        :type n: int
        :rtype: int
        """

        result = 0
        i = 1

        while i * (1+i) / 2 <= n:
            result += n % i == (0 if i % 2 else i / 2)
            i += 1

        return result


    def consecutiveNumbersSum2(self, n):
        """
        :type n: int
        :rtype: int
        """

        result = 1
        for i in range(2, int((2*n)**0.5)+1):
            result += n % i == (0 if i & 1 else i >> 1)

        return result