class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        result = 0

        for elem in s:
            result *= 26
            result += ord(elem) - 64

        return result