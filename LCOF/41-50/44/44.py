class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """

        index = 1
        result = 0
        digit_num = 9 * 10 ** (index - 1)

        while n > digit_num * index:
            n -= digit_num * index
            result += digit_num
            index += 1
            digit_num = 9 * 10 ** (index - 1)

        offset = n / index
        remainder = n - index * offset
        return int(str(result + offset + (remainder > 0))[remainder-1])