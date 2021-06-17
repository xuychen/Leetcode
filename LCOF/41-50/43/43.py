class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """

        counts = [0]
        index = 0
        result = 0

        while 10 ** (index + 1) <= n:
            not_one = counts[-1] * 9
            one = counts[-1] + 10 ** index
            counts.append(not_one + one)
            index += 1

        for i in range(index, -1, -1):
            large = 10 ** i
            value = n / large
            n -= value * large
            if value == 1:
                result += counts[i] + (n + 1)
            elif value > 1:
                result += value * counts[i] + large

        return result