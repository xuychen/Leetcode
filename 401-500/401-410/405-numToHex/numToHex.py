class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num < 0:
            num += 4294967296

        mapping = "0123456789abcdef"
        hexstring = ""

        while num > 0:
            hexstring = mapping[num % 16] + hexstring
            num /= 16

        return hexstring if hexstring else '0'