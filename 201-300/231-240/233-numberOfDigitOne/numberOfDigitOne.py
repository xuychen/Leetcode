class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """

        counts = [(1, 0)]
        index = 1
        result = 0

        while n >= pow(10, index):
            zeros = counts[-1][0] + 9 * counts[-1][1]
            ones = pow(10, index) + zeros
            counts.append((ones, zeros))
            index += 1

        for i in range(index-1, -1, -1):
            value = n / pow(10, i)
            n -= value * pow(10, i)
            if value == 1:
                result += counts[i][1] + n + 1
            elif value > 1:
                result += counts[i][0] + (value - 1) * counts[i][1]

        return result

            