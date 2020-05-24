class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        result = ""

        while n:
            n -= 1
            result += chr(n % 26 + 65)
            n /= 26

        return result[::-1]